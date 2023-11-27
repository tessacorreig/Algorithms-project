import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate


# In the following code we are creating the ‘Node’ class in a binary tree,
# which we will use to store the data from the dataset in our tree as it is
# the best data structure for this kind of data. The “key” of the binary of
# the tree would be the product timestamp.
class Node:
    def __init__(self, key, inventory, revenue, cost):
        self.key = key
        self.inventory = inventory
        self.revenue = revenue
        self.cost = cost
        self.left = None
        self.right = None
        self.height = 1


# We create an AVL tree class as it is a type of binary tree that has the
# special property of dynamic self-balancing with the benefits of a binary
# tree.
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

    # include in the ALV a function that will find the maximum timestamp
    # and minimum timestamp so it will later be told to the users
    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, root):
        if not root:
            return None

        current = root
        while current.left:
            current = current.left

        return current.key

    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, root):
        if not root:
            return None

        current = root
        while current.right:
            current = current.right

        return current.key

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

    # This is a method from the AVL tree which will allow to traverse the tree
    # inorder,and retrieve the adequate data based on the attribute chosen by
    # the user, and the time interval.
    # It will append to result object the nodes/ observations that fit the requirements.

    def inorder_traversal_filtered(self, node, start_timestamp, end_timestamp, attribute, result):
        if node:

            # transform intervals given by user to timestamps so we can compare them to key of nodes
            start_timestamp = pd.to_datetime(start_timestamp)
            end_timestamp = pd.to_datetime(end_timestamp)

            # traverse tree in order

            if start_timestamp <= node.key:
                self.inorder_traversal_filtered(node.left, start_timestamp, end_timestamp, attribute, result)

            if start_timestamp <= node.key <= end_timestamp:
                if attribute == 'inventory':
                    result.append((node.key, node.inventory))
                elif attribute == 'revenue':
                    result.append((node.key, node.revenue))
                elif attribute == 'cost':
                    result.append((node.key, node.cost))

            if node.key <= end_timestamp:
                self.inorder_traversal_filtered(node.right, start_timestamp, end_timestamp, attribute, result)




# The following code is used to process our dataset, in this function we
# include some error handling techniques as well as creating an AVL tree to
# store the data imported FPR EACH PRODUCT.
def read_data(filename):
    product_trees = {}

    df = pd.read_excel(filename)

    # Here we are setting all the elements in the ‘Product’ column to lowercase
    # as an error handling technique that will be essential for our program to
    # run properly.
    df['Product'] = df['Product'].str.lower()

    # This function is used to go through every row/ observation of the dataset
    for index, row in df.iterrows():
        product_name = row['Product']

        if product_name not in product_trees:
            product_trees[product_name] = AVLTree()

        avl_tree = product_trees[product_name]
        # Here we are creating a product Tree for ach new product the code finds
        # when reading the dataset and saving it to a dictionary (key is product name and
        # value is the product tree

        # In this part of the code we assign the values of the different columns of
        # the dataset to different attributes of each node in the product tree created
        # for that product (done above). This is done so that they can be used when making
        # plots/ tables. Additionally, we convert the ‘timestamp’ column to be of type ‘date’. We
        # do this because each node’s key will be the timestamp, which will
        # self-balance in the tree data structure so we have to be able to compare them
        key = row['Timestamp']
        key = pd.to_datetime(key)
        inventory = row['Inventory']
        revenue = row['AccumulatedRevenue']
        cost = row['AccumulatedCost']

        avl_tree.insert(key, inventory, revenue, cost)
        # here we are inserting the node with its respective attribues
        # defined above when reading the row
    return product_trees






# Next we will create a function that will take product data in the form
# of AVL trees, a specific product name, and a time interval. Then it will
# filter the data based on the specified time interval and product, create
# a DataFrame, and plot the filtered data in a table.

def plot_product_data(product_trees, product_name, start_timestamp, end_timestamp, attribute='inventory'):
    product_name = product_name.lower()
    if product_name not in product_trees:
        print(f"Product '{product_name}' not found.")
        return

    # here it retrieves the AVL tree for specified product using the product dictionary
    avl_tree = product_trees[product_name]

    data = []

    # in order traversal for avl tree (filtered), will save the filtered nodes
    # in data list created above
    avl_tree.inorder_traversal_filtered(avl_tree.root, start_timestamp, end_timestamp, attribute, data)

    # error handling message in case there was no data
    if not data:
        print(f"No data found for product '{product_name}' within the specified interval.")
        return

    # plot the table using the filtered data
    df = pd.DataFrame(data, columns=['timestamp', attribute])

    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df[attribute], marker='o')
    plt.title(f"{attribute.capitalize()} for Product {product_name} ({start_timestamp} to {end_timestamp})")
    plt.xlabel('Timestamp')
    plt.ylabel(attribute.capitalize())
    plt.grid(True)
    plt.show()





# Next we create a function that takes product data, also in form of AVL
# trees, a specific data name and a time interval , calls the filter
# function it based on the specification, creates a dataframe, sorts the
# data by timestamp so it can be seen clearly and displays the data finally
# in a formatted table using the tabulate function in the taabulate library.
def display_product_data_table(product_trees, product_name, start_timestamp, end_timestamp, attribute='inventory'):
    product_name = product_name.lower()
    if product_name not in product_trees:
        print(f"Product '{product_name}' not found.")
        return

    # retrieve data for AVL tree:
    avl_tree = product_trees[product_name]

    data = []

    # in order traversal for avl tree (filtered), will save the filtered nodes
    # in data list created above
    avl_tree.inorder_traversal_filtered(avl_tree.root, start_timestamp, end_timestamp, attribute, data)

    # This part of the code is for error handling, which will be used if the
    # user inputs an invalid input.
    if not data:
        print(f"No data found for product '{product_name}' within the specified interval.")
        return

    df = pd.DataFrame(data, columns=['timestamp', attribute])
    print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))





# Here we designed a function that will interact with the user, it will
# allow them to choose a product, specify a time interval and decide whether
# they want to see their product as a table or as a plot. For printing the
# available products and timestamp it will look into the data frame and
# extract the products and the timestamps available

def user_selection(product_trees, attribute_choice, table=False):
    attribute_mapping = {1: 'inventory', 2: 'revenue', 3: 'expenses'}
    attribute = attribute_mapping[attribute_choice]
    # We will use a variable called attribute which holds whether the user
    # wants to display inventory/revenue/ expenses
    # Given that the user is only typing options 1-3 from the menu options we
    # will convert these values using a dictionary.

    print("\nAvailable Products:")
    for product in product_trees.keys():
        print(f"- {product}")
    # We have a dictionary with the product names and each product tree as a
    # value. We will loop through the keys (the product names to display the
    # available products for the user to select.

    product_name = input("Enter the product name: ").lower()
    product_tree = product_trees[product_name]
    # We use the product_trees dictionary to access the product_tree desired
    # by the user, he provides the key which is the product name

    start_available = product_tree.find_min()
    end_available = product_tree.find_max()

    # To aid user understanding we will display the range of data times for
    # which we have available for the selected product. For this we will have to
    # use the find max and find min functions of the AVL tree. Because the key
    # is the timestamp it will display to the user the first and last
    # timestamp available for that product so that the user knows which time
    # intervals he can choose from.
    print()
    print()
    print("For", product_name, "we have data available from", start_available, "to", end_available)

    print("Please choose a time interval from the data available.")

    print()
    start_timestamp = input("Enter the start timestamp (YYYY-MM-DD): ")
    print()
    end_timestamp = input("Enter the end timestamp (YYYY-MM-DD): ")

    # depending on the choice of the user display the table or the graph
    if table:
        display_product_data_table(product_trees, product_name, start_timestamp, end_timestamp, attribute)
    else:
        plot_product_data(product_trees, product_name, start_timestamp, end_timestamp, attribute)


# Create the menu options for different categories. First we
# will display a menu with the options related to the different types of data.
# This is a general menu where the user will choose the type of data they
# want to work with:
def display_menu():
    print("MENU OPTIONS:")
    print("1. Inventory")
    print("2. Revenue")
    print("3. Expenses")
    print("4. Exit Program")
    print()


# display options users can choose to analyze their data related to
# inventory
def menu_inventory():
    print("Inventory OPTIONS:")
    print("1. Plot Graph (Filtered by Product and Time)")
    print("2. Plot Table (Filtered by Product and Time)")
    print()


# display options related to revenue, is where users will choose what they
# want to display according to revenue
def menu_revenue():
    print()
    print("Revenue OPTIONS:")
    print("1. Plot Graph (Filtered by Product and Time)")
    print("2. Plot Table (Filtered by Product and Time)")
    print()


# similar to the previous functions, this one displays options related to expenses.
def menu_expenses():
    print()
    print("Expenses OPTIONS:")
    print("1. Plot Graph (Filtered by Product and Time)")
    print("2. Plot Table (Filtered by Product and Time)")
    print()


# The main function will allow user to navigate to the program created; it
# will call the functions for the different menus, and use if statements
# to redirect the user based on their selections.
# It will also allow them to choose how they want to visualize their data.
# The program continues to run until the user decides to exit the program.


def main():
    file_path = 'startups.xlsx'
    product_trees = read_data(file_path)

    # infinite loop to make multiple selections  and redirect them back to main
    # menu after each plot until they want to exit the program (choice 4)
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-4, or any other number to exit): "))

        # check user choice and display corresponding menu
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
        # check user choice and display corresponding plot
        choice2 = int(input("Enter your choice (1-2): "))

        if choice2 == 1:
            user_selection(product_trees, choice)
        elif choice2 == 2:
            user_selection(product_trees, choice, table=True)


main()

