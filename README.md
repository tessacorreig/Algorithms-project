# Algorithms-project
Algorithms project for start up app

## Description:
Startup Tracker is a user-friendly app designed to help small startups and businesses effectively track their inventory levels, profits, and revenues. It's tailored for businesses that are just starting and don't have the resources for complex inventory management systems. Startup tracker is meant to allow small businesses to manage their  inventory and gain insights into financial performance, making it simpler to run businesses efficiently.

## Table of Contents
1. [Introduction] (#introduction)
2. [Installation & Usage] (#Installation-&-Usage)
3. [Further Improvements] (#further-improvements)
4. [Credits] (#credits)

# Introduction 
This application was created for our Algorithms & Data Structures class. The project instructions were to create an app using what we learned in class. 

We came up with StartupPal, an app that helps people with start-up businesses, to organize their inventories, and track their revenue and expenses efficiently. We mainly use AVL trees as our chosen binary search tree, as it balances itself. Since it is a binary search tree, we are able to filter the data computed, and use a divide and conquer approach to obtain the data the user requires. So far, the algorithm uses `Inventory`, `Accumulated Cost`,`Accumulated Revenue`, `Product`, and `Timestamp` as attributes to organize the start-up business effectively. 

## User journey 
The app is first accessed by a login in or sign up page for the user to save their data accordingly. After, a dashboard is displayed with a main statistics page of inventory levels, overall revenue and inventory. The dashboard displays whether the data is increasing or decreasing (an overview of all the data). From this dashboard, there are three tabs that can be accessed: Inventory, Revenues, and Expenses. 

To track inventories, the system displays the main site of an activated account where the menu is initially displayed. The system then allows to select the Inventory tab, and shows an initial graph with the total inventories of all products distinguishing between those bought this month and those bought previously. After this, if you double tap on the graph it can change to a table format which displays the different amounts of each product, for the user to visually understand it in a different manner. Also, the system is able to filter by allowing the user to select a specific product or group of products and specific time frames. the system will again display the inventory graph with the corresponding filtered inventories. If the user double taps it changes again to the table format. In addition, the inventories page, displays the savings of the start-up, by allowing the user to save the graphs they have created to a given format. 

As previously mentioned for inventories, the app tracks revenues and expenses similarly. For revenues, the system displays the main site of an activated account where the menu is initially displayed and the system the nallows to select the revenue tab. The system shows a graph with the total revenues, and can also change to table format to show the different amounts of each product. The system also filters and shows savings as previously mentioned. 

To track expenses, the system displays the main site and allows the user to select the expenses tab, where the system displays an initial graph with the total expenses of all products distinguishing between those bough this month and those bough previously. It does the same as with the other two previous tabs for filtering and savings. 

###Limitations
The algorithm is currently limited to start-up business, as if a business were to grow exponentially into a mass corporation, our current system might not hold all data structures appropriately. 

##File Architecture


#The Dataset
The dataset provides information about 4 products from a start-up with 208 accumulated different time stamps. Its content is relevant for anyone interested in tracking and organizing their products depending on their time stamps, and understand their current and past savings, expenses, incomes, and inventories. The following variables are presented:

- Product: including product A, B, C & D, with their respective different time stamps.
- Timestamp: there are 208 timestamps, each with their corresponding date and time.
- Inventory: there are different amounts of stock of the four product types, depending on the time stamp given.
- Accumulated Revenue: there are different amounts of revenue of the four product types, depending on the specific time stamp.
- Accumulated Cost: there are different amounts of costs of the four product types, depending on the given time stamp.

This dataset was manually constructed by our group, taking into account the workings of a start-up. 

# Installation & Usage 



# Further Improvements 



# Resources Used


# Credits


