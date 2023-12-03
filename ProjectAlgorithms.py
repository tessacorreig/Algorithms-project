
from graphics import *
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
from matplotlib.table import Table
import csv

#### Read data and start Button ####

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
        # value is the product tree)

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


def startButton(win):
    title = Text(Point(2, 3.5), "StartUpPal")
    title.setSize(30)
    title.setStyle("bold")
    title.setFace("courier")
    title.draw(win)

    title2 = Text(Point(2, 3.25), "Application")
    title2.setSize(20)
    title2.setFace("courier")
    title2.draw(win)

    start = Rectangle(Point(1,1.5), Point(3,2.5))
    start.setFill("lightgrey")
    start.draw(win)

    startText= Text(Point(2,2), "START")
    startText.setSize(30)
    startText.setStyle("bold")
    startText.setFace("courier")
    startText.draw(win)

    while True:
        pt = win.getMouse()
        if pt:
            if pt.getX() > 1 and pt.getX() < 3:
                if pt.getY() > 1 and pt.getY() < 3:
                    start.undraw()
                    startText.undraw()
                    title.undraw()
                    title2.undraw()
                    break


###LOG IN and SIGN IN ####
def credentialsFileCreator():
    initial_credentials = [
        ['user1', 'password1'],
        ['user2', 'password2'],
        ['user3', 'password3'],
    ]

    filePath = 'credentials.csv'

    try:
        with open(filePath, mode='r') as file:
            print(f'Credentials file: "{filePath}" already exists.')
    except FileNotFoundError:
        with open(filePath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(initial_credentials)
        print(f'Created credentials file: "{filePath}"')


def signUp(username, password):
    with open('credentials.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

def login(username, password):
    with open('credentials.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
    return False

def checkExistingUser(username):
    with open('credentials.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return True
    return False

def openPage():
    win1 = GraphWin("Start Page", 500, 500)
    notClicked = True

    titleSpace = Rectangle(Point(100,50), Point(400, 150))
    titleSpace.setFill(color_rgb(233,233,233))
    titleSpace.draw(win1)
    titleLabel = Text(Point(250, 100), "StartuPal")
    titleLabel.setStyle("bold")
    titleLabel.setSize(30)
    titleLabel.draw(win1)

    loginSpace = Rectangle(Point(150,200), Point(350, 250))
    loginSpace.setFill(color_rgb(233,233,233))
    loginSpace.draw(win1)
    loginLabel = Text(Point(250, 225), "Log In")
    loginLabel.setStyle("bold")
    loginLabel.setSize(24)
    loginLabel.draw(win1)

    signinSpace = Rectangle(Point(150,260), Point(350, 310))
    signinSpace.setFill(color_rgb(233,233,233))
    signinSpace.draw(win1)
    signinLabel = Text(Point(250, 285), "Sign In")
    signinLabel.setStyle("bold")
    signinLabel.setSize(24)
    signinLabel.draw(win1)

    exitSpace = Rectangle(Point(150,320), Point(350, 370))
    exitSpace.setFill(color_rgb(233,233,233))
    exitSpace.draw(win1)
    exitLabel = Text(Point(250, 345), "Exit")
    exitLabel.setStyle("bold")
    exitLabel.setSize(24)
    exitLabel.draw(win1)

    while notClicked:
        pt = win1.getMouse()
        if pt.getX() >= 150 and pt.getX() <= 350:
            if pt.getY() >= 200 and pt.getY() <= 250:
                notClicked = False
                win1.close()
                loginPage()
        if pt.getX() >= 150 and pt.getX() <= 350:
            if pt.getY() >= 260 and pt.getY() <= 310:
                notClicked = False
                win1.close()
                signinPage()
        if pt.getX() >= 150 and pt.getX() <= 350:
            if pt.getY() >= 320 and pt.getY() <= 370:
                notClicked = False
                win1.close()

    win1.close()

def loginPage():
    win1 = GraphWin("Log In Page", 500, 500)
    notClicked = True

    def backButtonClicked(click, backButton):
        if click:
            p = click
            x1, y1, x2, y2 = backButton.getP1().getX(), backButton.getP1().getY(), backButton.getP2().getX(), backButton.getP2().getY()
            if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
                return True
        return False

    def loginButtonClicked(click, loginButton):
        if click:
            p = click
            x1, y1, x2, y2 = loginButton.getP1().getX(), loginButton.getP1().getY(), loginButton.getP2().getX(), loginButton.getP2().getY()
            if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
                return True
        return False

    def errorMessage():
        warningLabel = Text(Point(250, 325), "Wrong User or Password")
        warningLabel.setSize(16)
        warningLabel.setTextColor("red")
        warningLabel.draw(win1)

    titleSpace = Rectangle(Point(100,50), Point(400, 150))
    titleSpace.setFill(color_rgb(233,233,233))
    titleSpace.draw(win1)
    titleLabel = Text(Point(250, 100), "Log In Page")
    titleLabel.setStyle("bold")
    titleLabel.setSize(30)
    titleLabel.draw(win1)

    usernameLabel = Text(Point(170, 200), "Enter Username Here:")
    usernameLabel.setSize(18)
    usernameLabel.draw(win1)
    usernameSpace = Rectangle(Point(80, 210), Point(420, 240))
    usernameSpace.setFill("white")
    usernameSpace.draw(win1)

    inputUserName = Entry(Point(250, 225), 46)
    inputUserName.setFill("white")
    inputUserName.draw(win1)

    passwordLabel = Text(Point(170, 275), "Enter Password Here:")
    passwordLabel.setSize(18)
    passwordLabel.draw(win1)
    passwordSpace = Rectangle(Point(80, 285), Point(420, 315))
    passwordSpace.setFill("white")
    passwordSpace.draw(win1)

    inputUserPassword = Entry(Point(250, 300), 46)
    inputUserPassword.setFill("white")
    inputUserPassword.draw(win1)

    loginButton = Rectangle(Point(260, 360), Point(360, 400))
    loginButton.setFill(color_rgb(20, 230, 111))
    loginButton.draw(win1)
    loginLabel = Text(Point(310, 380), "Log In")
    loginLabel.setSize(22)
    loginLabel.draw(win1)

    backButton = Rectangle(Point(140, 360), Point(240, 400))
    backButton.setFill(color_rgb(230, 20, 20))
    backButton.draw(win1)
    backLabel = Text(Point(190, 380), "Back")
    backLabel.setSize(22)
    backLabel.draw(win1)

    while True:
        click = win1.getMouse()

        if backButtonClicked(click, backButton):
            win1.close()
            openPage()
            break

        if loginButtonClicked(click, loginButton):
            userName = inputUserName.getText()
            userPassword = inputUserPassword.getText()
            if userName and userPassword:
                if login(userName, userPassword):
                    notClicked = False
                    win1.close()
                    break
                else:
                    errorMessage()

    win1.close()

def signinPage():
    win1 = GraphWin("Sign In Page", 500, 500)
    win1.setBackground(color_rgb(241, 255, 191))
    notClicked = True

    def backButtonClicked(click, backButton):
        if click:
            p = click
            x1, y1, x2, y2 = backButton.getP1().getX(), backButton.getP1().getY(), backButton.getP2().getX(), backButton.getP2().getY()
            if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
                return True
        return False

    def signinButtonClicked(click, loginButton):
        if click:
            p = click
            x1, y1, x2, y2 = loginButton.getP1().getX(), loginButton.getP1().getY(), loginButton.getP2().getX(), loginButton.getP2().getY()
            if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
                return True
        return False

    def errorMessage():
        warningLabel = Text(Point(250, 325), "User already exists")
        warningLabel.setSize(16)
        warningLabel.setTextColor("red")
        warningLabel.draw(win1)

    titleSpace = Rectangle(Point(100,50), Point(400, 150))
    titleSpace.setFill(color_rgb(233,233,233))
    titleSpace.draw(win1)
    titleLabel = Text(Point(250, 100), "Sign In Page")
    titleLabel.setStyle("bold")
    titleLabel.setSize(30)
    titleLabel.draw(win1)

    usernameLabel = Text(Point(190, 200), "Enter New Username Here:")
    usernameLabel.setSize(18)
    usernameLabel.draw(win1)
    usernameSpace = Rectangle(Point(80, 210), Point(420, 240))
    usernameSpace.setFill("white")
    usernameSpace.draw(win1)

    inputUserName = Entry(Point(250, 225), 46)
    inputUserName.setFill("white")
    inputUserName.draw(win1)

    passwordLabel = Text(Point(190, 275), "Enter New Password Here:")
    passwordLabel.setSize(18)
    passwordLabel.draw(win1)
    passwordSpace = Rectangle(Point(80, 285), Point(420, 315))
    passwordSpace.setFill("white")
    passwordSpace.draw(win1)

    inputUserPassword = Entry(Point(250, 300), 46)
    inputUserPassword.setFill("white")
    inputUserPassword.draw(win1)

    signinButton = Rectangle(Point(260, 360), Point(360, 400))
    signinButton.setFill(color_rgb(20, 230, 111))
    signinButton.draw(win1)
    signinLabel = Text(Point(310, 380), "Sign In")
    signinLabel.setSize(22)
    signinLabel.draw(win1)

    backButton = Rectangle(Point(140, 360), Point(240, 400))
    backButton.setFill(color_rgb(230, 20, 20))
    backButton.draw(win1)
    backLabel = Text(Point(190, 380), "Back")
    backLabel.setSize(22)
    backLabel.draw(win1)

    while True:
        click = win1.getMouse()

        if backButtonClicked(click, backButton):
            win1.close()
            openPage()
            break

        if signinButtonClicked(click, signinButton):
            userName = inputUserName.getText()
            userPassword = inputUserPassword.getText()
            if userName and userPassword:
                if checkExistingUser(userName):
                    errorMessage()
                else:
                    signUp(userName, userPassword)
                    notClicked = False
                    win1.close()
                    break

    win1.close()


#####CODE TO CREATE DATASTRUCTURE AVL TREE

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


########## Create user interfaces for menus for user to choose
def create_button(win, label, p1, p2):
    button = Rectangle(p1, p2)
    button.setFill("lightgrey")
    button.draw(win)

    text_point = Point((p1.getX() + p2.getX()) / 2, (p1.getY() + p2.getY()) / 2)
    text = Text(text_point, label)
    text.setFace("courier")
    text.setSize(15)
    text.draw(win)

    return button, text

def undrawbuttons(*elements):
    for element in elements:
        element.undraw()

def choose_dataset(win):
    title = Text(Point(2, 3.5), "Choose Dataset")
    title.setSize(30)
    title.setFace("courier")
    title.setStyle("bold")
    title.draw(win)

    button_from_files, label_from_files = create_button(win, "From my files", Point(1, 2.5), Point(3, 3))
    button_default, label_default = create_button(win, "Default Dataset", Point(1, 1.5), Point(3, 2))

    while True:
        click_point = win.getMouse()
        if button_from_files.getP1().getX() < click_point.getX() < button_from_files.getP2().getX() and \
                button_from_files.getP1().getY() < click_point.getY() < button_from_files.getP2().getY():
            undrawbuttons(button_from_files, label_from_files, button_default, label_default, title)
            return 1

        elif button_default.getP1().getX() < click_point.getX() < button_default.getP2().getX() and \
                button_default.getP1().getY() < click_point.getY() < button_default.getP2().getY():
            undrawbuttons(button_from_files, label_from_files, button_default, label_default, title)
            return 2


def DisplayMenu(win):
    title = Text(Point(2, 3.5), "MAIN MENU")
    title.setSize(30)
    title.setFace("courier")
    title.setStyle("bold")
    title.draw(win)

    button_inventory, label_inventory = create_button(win, "Inventory", Point(1, 2.5), Point(3, 3))
    button_revenue, label_revenue = create_button(win, "Revenue", Point(1, 1.5), Point(3, 2))
    button_expenses, label_expenses = create_button(win, "Expenses", Point(1, 0.5), Point(3, 1))

    while True:
        click_point = win.getMouse()
        if button_inventory.getP1().getX() < click_point.getX() < button_inventory.getP2().getX() and \
                button_inventory.getP1().getY() < click_point.getY() < button_inventory.getP2().getY():
            undrawbuttons(button_inventory, label_inventory, button_revenue, label_revenue, button_expenses, label_expenses, title)
            return 1

        elif button_revenue.getP1().getX() < click_point.getX() < button_revenue.getP2().getX() and \
                button_revenue.getP1().getY() < click_point.getY() < button_revenue.getP2().getY():
            undrawbuttons(button_inventory, label_inventory, button_revenue, label_revenue, button_expenses, label_expenses, title)
            return 2

        elif button_expenses.getP1().getX() < click_point.getX() < button_expenses.getP2().getX() and \
                button_expenses.getP1().getY() < click_point.getY() < button_expenses.getP2().getY():
            undrawbuttons(button_inventory, label_inventory, button_revenue, label_revenue, button_expenses, label_expenses, title)
            return 3

def optionsMenu(win):
    title = Text(Point(2, 3.5), "SELECT AN OPTION")
    title.setSize(30)
    title.setFace("courier")
    title.setStyle("bold")
    title.draw(win)

    button_plot_graph, label_plot_graph = create_button(win, "Plot Graph", Point(1, 2.5), Point(3, 3))
    button_plot_table, label_plot_table = create_button(win, "Plot Table", Point(1, 1.5), Point(3, 2))

    while True:
        click_point = win.getMouse()
        if button_plot_graph.getP1().getX() < click_point.getX() < button_plot_graph.getP2().getX() and \
                button_plot_graph.getP1().getY() < click_point.getY() < button_plot_graph.getP2().getY():
            undrawbuttons(button_plot_graph, label_plot_graph, button_plot_table, label_plot_table, title)
            return "plot_graph"

        elif button_plot_table.getP1().getX() < click_point.getX() < button_plot_table.getP2().getX() and \
                button_plot_table.getP1().getY() < click_point.getY() < button_plot_table.getP2().getY():
            undrawbuttons(button_plot_graph, label_plot_graph, button_plot_table, label_plot_table, title)
            return "plot_table"

##### Functions to get product selections for tables and graphs
# Here we designed  functions that will interact with the user, it will
# allow them to choose a product, specify a time interval and decide whether
# they want to see their product as a table or as a plot. For printing the
# available products and timestamp it will look into the data frame and
# extract the products and the timestamps available by checking the product trees.
def get_product_name_window(product_trees):
    win = GraphWin("Product Selection", 500, 400)

    text = Text(Point(250, 30), "Available Products:")
    text.setStyle("bold")
    text.setFace("courier")
    text.setSize(14)
    text.draw(win)

    y_position = 60
    product_buttons = []  # To store the product buttons

    for product in product_trees.keys():
        button, _ = create_button(win, f"Select {product}", Point(50, y_position), Point(450, y_position + 30))
        product_buttons.append((button, product))
        y_position += 30

    submit_button, submit_text = create_button(win, "Exit", Point(200, 350), Point(300, 380))

    while True:
        click_point = win.getMouse()

        # Check if any product button is clicked
        for button, product in product_buttons:
            if button.getP1().getX() < click_point.getX() < button.getP2().getX() and \
                    button.getP1().getY() < click_point.getY() < button.getP2().getY():
                win.close()
                return product.lower()

        if submit_button.getP1().getX() < click_point.getX() < submit_button.getP2().getX() and \
                submit_button.getP1().getY() < click_point.getY() < submit_button.getP2().getY():
            win.close()
            return None

def get_interval_window(product_name, product_trees):
    win = GraphWin("Interval Selection", 600, 500)

    start_available = product_trees[product_name].find_min()
    end_available = product_trees[product_name].find_max()

    info_text = Text(Point(300, 50), f"For {product_name}, data is available")
    info_text.setFace("courier")
    info_text.setStyle("bold")
    info_text.setSize(18)
    info_text.draw(win)

    info_text2 = Text(Point(300, 80), f"from {start_available} to {end_available}.")
    info_text2.setFace("courier")
    info_text2.setStyle("bold")
    info_text2.setSize(18)
    info_text2.draw(win)

    start_label = Text(Point(180, 150), "Start timestamp (YYYY-MM-DD):")
    start_label.setFace("courier")
    start_label.setSize(18)
    start_label.draw(win)

    start_input = Entry(Point(450, 150), 20)
    start_input.draw(win)

    end_label = Text(Point(180, 200), "End timestamp (YYYY-MM-DD):")
    end_label.setSize(18)
    end_label.setFace("courier")
    end_label.draw(win)

    end_input = Entry(Point(450, 200), 20)
    end_input.draw(win)

    submit_button, submit_text = create_button(win, "Submit", Point(250, 250), Point(350, 280))
    exit_button, exit_text = create_button(win, "Exit", Point(400, 250), Point(500, 280))

    while True:
        click_point = win.getMouse()
        if submit_button.getP1().getX() < click_point.getX() < submit_button.getP2().getX() and \
                submit_button.getP1().getY() < click_point.getY() < submit_button.getP2().getY():
            start_timestamp = start_input.getText()
            end_timestamp = end_input.getText()
            undrawbuttons(info_text, info_text2, start_label, start_input, end_label, end_input, submit_button,
                          submit_text, exit_button, exit_text)
            win.close()
            return start_timestamp, end_timestamp
        elif exit_button.getP1().getX() < click_point.getX() < exit_button.getP2().getX() and \
                exit_button.getP1().getY() < click_point.getY() < exit_button.getP2().getY():
            win.close()
            return None, None


##### Plot tables and Graphs #####
def draw_plot(product_trees, product_name, start_timestamp, end_timestamp, attribute='inventory', table=False):
    if table:
        display_product_data_table(product_trees, product_name, start_timestamp, end_timestamp, attribute)
    else:
        plot_product_data(product_trees, product_name, start_timestamp, end_timestamp, attribute)


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

def display_product_data_table(product_trees, product_name, start_timestamp, end_timestamp, attribute='inventory',fontsize=14):
    product_name = product_name.lower()
    if product_name not in product_trees:
        print(f"Product '{product_name}' not found.")
        return

    # Retrieve data for AVL tree
    avl_tree = product_trees[product_name]

    data = []

    # Conduct an inorder traversal on the AVL tree
    avl_tree.inorder_traversal_filtered(avl_tree.root, start_timestamp, end_timestamp, attribute, data)

    if not data:
        print(f"No data found for product '{product_name}' within the specified interval.")
        return

    df = pd.DataFrame(data, columns=['timestamp', attribute])
    df.sort_values(by='timestamp', inplace=True)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(30, 15))

    # Hide the axes
    ax.axis('off')

    # Create the table
    table_data = [df.columns] + df.values.tolist()
    table = Table(ax, bbox=[0, 0, 1, 1])

    # Add cell content to the table
    for i, row in enumerate(table_data):
        for j, cell in enumerate(row):
            table.add_cell(i, j, 0.1, 0.1, text=cell, loc='center', facecolor='none')

    # Add the table to the figure
    ax.add_table(table)

    plt.title(f"{attribute.capitalize()} Table for Product {product_name} ({start_timestamp} to {end_timestamp})")
    plt.show()

#### Function that allows user to go back to menu
def End_or_Repeat(win):
    title = Text(Point(2, 1.5), "SELECTED VISUALISATION SHOULD OPEN UP")
    title.setSize(20)
    title.setStyle("bold")
    title.setFace("courier")
    title.draw(win)
    button_start, label_start = create_button(win, "Back to Menu", Point(1, 3), Point(3, 3.5))
    button_end, label_end = create_button(win, "Quit", Point(1, 2.5), Point(3, 3))

    while True:
        click_point = win.getMouse()
        if button_start.getP1().getX() < click_point.getX() < button_start.getP2().getX() and \
                button_start.getP1().getY() < click_point.getY() < button_start.getP2().getY():
            undrawbuttons(button_start, label_start, button_end, label_end, title)
            return 1

        elif button_end.getP1().getX() < click_point.getX() < button_end.getP2().getX() and \
                button_end.getP1().getY() < click_point.getY() < button_end.getP2().getY():
            undrawbuttons(button_start, label_start, button_end, label_end, title)
            return 2


##### Main function ####
def main():
    credentialsFileCreator()
    win = GraphWin("StartUpPal", 500, 500)
    win.setCoords(0.0, 0.0, 4.0, 4.5)
    win.setBackground('white')

    startButton(win)
    openPage()

    data = choose_dataset(win)
    if data == 1:
        root = Tk()
        root.withdraw()  # Hide the main window

        # Ask the user to select a file
        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel files", "*.xlsx")],
            initialfile='startups.xlsx'  # Set the default file
        )
    if data == 2:
        file_path = "startups.xlsx"

    product_trees = read_data(file_path)

    while True:
        selection = DisplayMenu(win)
        visualisation = optionsMenu(win)

        if visualisation == "plot_table":

            product_name = get_product_name_window(product_trees)
            if product_name:
                start_timestamp, end_timestamp = get_interval_window(product_name, product_trees)
                if start_timestamp and end_timestamp:
                    draw_plot(product_trees, product_name, start_timestamp, end_timestamp, attribute='inventory',
                              table=True)
        elif visualisation == "plot_graph":
            product_name = get_product_name_window(product_trees)
            if product_name:
                start_timestamp, end_timestamp = get_interval_window(product_name, product_trees)
                if start_timestamp and end_timestamp:
                    draw_plot(product_trees, product_name, start_timestamp, end_timestamp, attribute='inventory',
                              table=False)

        End_or_Repeat(win)


if _name_ == "_main_":
    main()
