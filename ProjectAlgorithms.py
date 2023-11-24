import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate




class Node:
  def __init__(self, key, inventory, revenue, cost):
      self.key = key
      self.inventory = inventory
      self.revenue = revenue
      self.cost = cost
      self.left = None
      self.right = None
      self.height = 1
class AVLTree:
  def __init__(self):
      self.root = None

  def insert(self, key, inventory, revenue, cost):
      self.root = self._insert(self.root, key, inventory, revenue, cost)

  def _insert(self, root, key, inventory, revenue, cost):
      if not root:
          return Node(key, inventory, revenue, cost)
      elif key < root.key:
          root.left = self._insert(root.left, key, inventory, revenue, cost)
      else:
          root.right = self._insert(root.right, key, inventory, revenue, cost)
      root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
      balance = self.get_balance(root)
      if balance > 1 and key < root.left.key:
          return self.right_rotate(root)
      if balance < -1 and key > root.right.key:
          return self.left_rotate(root)
      if balance > 1 and key > root.left.key:
          root.left = self.left_rotate(root.left)
          return self.right_rotate(root)
      if balance < -1 and key < root.right.key:
          root.right = self.right_rotate(root.right)
          return self.left_rotate(root)
      return root
  def left_rotate(self, y):
      x = y.right
      T2 = x.left
      x.left = y
      y.right = T2
      y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
      x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
      return x
  def right_rotate(self, x):
      y = x.left
      T2 = y.right
      y.right = x
      x.left = T2
      x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
      y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
      return y
  def get_balance(self, node):
      if not node:
          return 0
      return self.get_height(node.left) - self.get_height(node.right)
  def get_height(self, node):
      if not node:
          return 0
      return node.height
  def inorder_traversal_filtered(self, node, start_timestamp, end_timestamp, attribute, result):
      if node:
          start_timestamp= pd.to_datetime(start_timestamp)
          end_timestamp = pd.to_datetime(end_timestamp)
          if start_timestamp <= node.key <= end_timestamp:
              if attribute == 'inventory':
                  result.append((node.key, node.inventory))
              elif attribute == 'revenue':
                  result.append((node.key, node.revenue))
              elif attribute == 'cost':
                  result.append((node.key, node.cost))
              self.inorder_traversal_filtered(node.left, start_timestamp, end_timestamp, attribute, result)
              self.inorder_traversal_filtered(node.right, start_timestamp, end_timestamp, attribute, result)
          elif node.key < start_timestamp:
              self.inorder_traversal_filtered(node.right, start_timestamp, end_timestamp, attribute, result)
          else:
              self.inorder_traversal_filtered(node.left, start_timestamp, end_timestamp, attribute, result)
def read_data(filename):
  product_trees = {}
  df = pd.read_excel(filename)
  df['Product'] = df['Product'].str.lower()
  for index, row in df.iterrows():
      product_name = row['Product']
      if product_name not in product_trees:
          product_trees[product_name] = AVLTree()
      avl_tree = product_trees[product_name]
      key = row['Timestamp']
      key = pd.to_datetime(key)
      inventory = row['Inventory']
      revenue = row['AccumulatedRevenue']
      cost = row['AccumulatedCost']
      avl_tree.insert(key, inventory, revenue, cost)
  return product_trees
def plot_product_data(product_trees, product_name, start_timestamp, end_timestamp, attribute='inventory'):
  product_name = product_name.lower()
  if product_name not in product_trees:
      print(f"Product '{product_name}' not found.")
      return
  avl_tree = product_trees[product_name]
  data = []
  avl_tree.inorder_traversal_filtered(avl_tree.root, start_timestamp, end_timestamp, attribute, data)
  if not data:
      print(f"No data found for product '{product_name}' within the specified interval.")
      return
  df = pd.DataFrame(data, columns=['timestamp', attribute])
  df.sort_values(by='timestamp', inplace=True)
  plt.figure(figsize=(10, 6))
  plt.plot(df['timestamp'], df[attribute], marker='o')
  plt.title(f"{attribute.capitalize()} for Product {product_name} ({start_timestamp} to {end_timestamp})")
  plt.xlabel('Timestamp')
  plt.ylabel(attribute.capitalize())
  plt.grid(True)
  plt.show()
def display_product_data_table(product_trees, product_name, start_timestamp, end_timestamp, attribute='inventory'):
  product_name = product_name.lower()
  if product_name not in product_trees:
      print(f"Product '{product_name}' not found.")
      return
  avl_tree = product_trees[product_name]
  data = []
  avl_tree.inorder_traversal_filtered(avl_tree.root, start_timestamp, end_timestamp, attribute, data)
  if not data:
      print(f"No data found for product '{product_name}' within the specified interval.")
      return
  df = pd.DataFrame(data, columns=['timestamp', attribute])
  df.sort_values(by='timestamp', inplace=True)
  print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
def user_selection(product_trees, attribute_choice, table=False):
  attribute_mapping = {1: 'inventory', 2: 'revenue', 3: 'expenses'}
  attribute = attribute_mapping[attribute_choice]
  print("\nAvailable Products:")
  for product in product_trees.keys():
      print(f"- {product}")
  product_name = input("Enter the product name: ").lower()
  product_mapping= {'product_a': '2023-01-01 to 2023-11-30', 'product_b': '2023-05-01 to 2023-12-21',
                    'product_c': '2023-01-01 to 2023-12-14', 'product_d': '2023-01-01 to 2023-12-21' }
  timeavailable = product_mapping[product_name]
  print()
  print()
  print("For", product_name, "we have data available from", timeavailable)
  print("Please choose a time interval from the data available.")
  print()
  start_timestamp = input("Enter the start timestamp (YYYY-MM-DD): ")
  print()
  end_timestamp = input("Enter the end timestamp (YYYY-MM-DD): ")
  if table:
      display_product_data_table(product_trees, product_name, start_timestamp, end_timestamp, attribute)
  else:
      plot_product_data(product_trees, product_name, start_timestamp, end_timestamp, attribute)
def display_menu():
  print("MENU OPTIONS:")
  print("1. Inventory")
  print("2. Revenue")
  print("3. Expenses")
  print("4. Exit Program")
  print()
def menu_inventory():
  print("Inventory OPTIONS:")
  print("1. Plot Graph (Filtered by Product and Time)")
  print("2. Plot Table (Filtered by Product and Time)")
  print()
def menu_revenue():
   print()
   print("Revenue OPTIONS:")
   print("1. Plot Graph (Filtered by Product and Time)")
   print("2. Plot Table (Filtered by Product and Time)")
   print()
def menu_expenses():
   print()
   print("Expenses OPTIONS:")
   print("1. Plot Graph (Filtered by Product and Time)")
   print("2. Plot Table (Filtered by Product and Time)")
   print()
def main():
  file_path = 'startups.xlsx'
  product_trees = read_data(file_path)
  while True:
      display_menu()
      choice = int(input("Enter your choice (1-4, or any other number to exit): "))
      if choice not in range(1, 4):
          print("Exiting the program.")
          break
      if choice == 1:
          menu_inventory()
      elif choice == 2:
          menu_revenue()
      elif choice == 3:
          menu_expenses()
      elif choice == 4:
          break
      choice2 = int(input("Enter your choice (1-2): "))
      if choice2 == 1:
          user_selection(product_trees, choice)
      elif choice2 == 2:
          user_selection(product_trees, choice, table=True)
main()
