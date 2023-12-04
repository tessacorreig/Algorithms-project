# Algorithms-project
Algorithms project for start up app

## Description:
Startup Tracker is a user-friendly app designed to help small startups and businesses effectively track their inventory levels, profits, and revenues. It's tailored for businesses that are just starting and don't have the resources for complex inventory management systems. Startup tracker is meant to allow small businesses to manage their  inventory and gain insights into financial performance, making it simpler to run businesses efficiently.

##balsamiq app 
A balsamiq app that uses templates and reads data to create our interface for our app algorithms. 
</table>
  </tr>
    </td>
      <img src= "https://github.com/alexiachm/Algorithms-project/blob/main/2174022b-7f21-49da-b26a-865c0e618425.jpg" alt="Sign in home screen" title= "Sign in home screen">
     </td>
     </td>
       <img src="https://github.com/alexiachm/Algorithms-project/blob/main/2e87ee98-1011-44dd-9bab-a33cfdcc6024.jpg" alt="Inventory" title= "Inventory">
     </td>
     </td>
       <img src="https://github.com/alexiachm/Algorithms-project/blob/main/35f6394f-7ac0-42be-8860-1564bb33a8d6.jpg" alt="Expenses" title= "Expenses">
      </td>
       </td>
        <img src="https://github.com/alexiachm/Algorithms-project/blob/main/WhatsApp%20Image%202023-11-24%20at%2016.41.54.jpeg" alt="Revenue" title= "Revenue">
      </td>
    </tr>

    <tr>
      <td> Sign in Home Screen</td>
      <td> Inventory</td>
      <td> Expenses</td>
      <td> Revenue</td>
    </tr>
  </table>
        


## Table of Contents
1. [Introduction](https://github.com/alexiachm/Algorithms-project/blob/main/README.md#introduction)
2. [Installation & Usage](https://github.com/alexiachm/Algorithms-project/blob/main/README.md#installation--usage)
3. [Further Improvements](https://github.com/alexiachm/Algorithms-project/blob/main/README.md#further-improvements-for-second-code)
4. [Credits](https://github.com/alexiachm/Algorithms-project/blob/main/README.md#credits)

# Introduction 
This application was created for our Algorithms & Data Structures class. The project instructions were to create an app using what we learned in class. 

We came up with StartupPal, an app that helps people with start-up businesses, to organize their inventories, and track their revenue and expenses efficiently. We mainly use AVL trees as our chosen binary search tree, as it balances itself. Since it is a binary search tree, we are able to filter the data computed, and use a divide and conquer approach to obtain the data the user requires. So far, the algorithm uses `Inventory`, `Accumulated Cost`,`Accumulated Revenue`, `Product`, and `Timestamp` as attributes to organize the start-up business effectively. 

## User journey 
The app is first accessed by a login in or sign up page for the user to save their data accordingly. After, a dashboard is displayed with a main statistics page of inventory levels, overall revenue and inventory. The dashboard displays whether the data is increasing or decreasing (an overview of all the data). From this dashboard, there are three tabs that can be accessed: Inventory, Revenues, and Expenses. 
<img src="https://github.com/alexiachm/Algorithms-project/blob/main/WhatsApp%20Image%202023-11-24%20at%2016.41.54.jpeg" alt="Revenue" title= "Revenue">

To track inventories, the system displays the main site of an activated account where the menu is initially displayed. The system then allows to select the Inventory tab, and shows an initial graph with the total inventories of all products distinguishing between those bought this month and those bought previously. After this, if you double tap on the graph it can change to a table format which displays the different amounts of each product, for the user to visually understand it in a different manner. Also, the system is able to filter by allowing the user to select a specific product or group of products and specific time frames. the system will again display the inventory graph with the corresponding filtered inventories. If the user double taps it changes again to the table format. In addition, the inventories page, displays the savings of the start-up, by allowing the user to save the graphs they have created to a given format. 
  <img src= "https://github.com/alexiachm/Algorithms-project/blob/main/2174022b-7f21-49da-b26a-865c0e618425.jpg" alt="Sign in home screen" title= "Sign in home screen">

As previously mentioned for inventories, the app tracks revenues and expenses similarly. For revenues, the system displays the main site of an activated account where the menu is initially displayed and the system the nallows to select the revenue tab. The system shows a graph with the total revenues, and can also change to table format to show the different amounts of each product. The system also filters and shows savings as previously mentioned. 
   <img src="https://github.com/alexiachm/Algorithms-project/blob/main/2e87ee98-1011-44dd-9bab-a33cfdcc6024.jpg" alt="Inventory" title= "Inventory">  

To track expenses, the system displays the main site and allows the user to select the expenses tab, where the system displays an initial graph with the total expenses of all products distinguishing between those bough this month and those bough previously. It does the same as with the other two previous tabs for filtering and savings.
<img src="https://github.com/alexiachm/Algorithms-project/blob/main/35f6394f-7ac0-42be-8860-1564bb33a8d6.jpg" alt="Expenses" title= "Expenses">
      </td>
       </td>

###Limitations
The algorithm is currently limited to start-up business, as if a business were to grow exponentially into a mass corporation, our current system might not hold all data structures appropriately. 
Our main limitation is that our app works specifically with our dataset only, if a startup would want to include their own dataset it would not be possible. 

##File Architecture
- `startups.py` - The main balsamiq app file that includes
- `templates`- the app contains templates to create the interfaces of the app
- any other files are self-explanatory.

#The Dataset
The dataset provides information about 4 products from a start-up with 208 accumulated different time stamps. Its content is relevant for anyone interested in tracking and organizing their products depending on their time stamps, and understand their current and past savings, expenses, incomes, and inventories. The following variables are presented:

- Product: including product A, B, C & D, with their respective different time stamps.
- Timestamp: there are 208 timestamps, each with their corresponding date and time.
- Inventory: there are different amounts of stock of the four product types, depending on the time stamp given.
- Accumulated Revenue: there are different amounts of revenue of the four product types, depending on the specific time stamp.
- Accumulated Cost: there are different amounts of costs of the four product types, depending on the given time stamp.

This dataset was manually constructed by our group, taking into account the workings of a start-up. 

# Installation & Usage 
#first-time install 

clone the files:
`````
git clone https://github.com/alexiachm/Algorithms-project.git
`````
creating and activating a virtual environment 
create the venv:
`````
cd Algorithms-project
python3 -m venv./Algorithms-project
`````

activating the venv (each time you open):
`````
source ./Algorithms-project/bin/activate 
`````

install modules:
`````
pip install -r requirements.txt 
`````
##usage 
`````
cd Algorithms-project
`````
`````
export FLASK_APP = app
`````
`````
export FLASK_DEBUG=1
`````
`````
flask run
`````

# Further improvements 
- for the code to be able to expand even further to help any business, and not only start ups

For our next steps, we thought about two main ideas which could be implemented in the long run. 

The first one includes Dataset improvements, such as:
- For our app to be able to take as an input datasets that don’t need to be in our specified format, but that the app manages to adapt to more structures of different datasets
as well as for our app to be able to handle bigger amounts of data, with more columns and rows.

The second one inludes taking into account big companies and not only start-ups:
- As an aim for our tracker to grow and be able to accompany businesses that were once startups, and are now large companies
And lastly, for our tracker to hold large amounts of data from big businesses, not only start-ups, so that our app would grow professionally and continue being of use for all businesses, including those that started organizing themselves with us. 

Also If our app was connected to the user’s dataset in real time we would provide valuable insights on the data such us:
- Notifications whenever inventory is below 0, or even before that so user’s don’t run out of inventory
- Updates on best performing products based on revenue
- Recommendations on which products to maintain for next operating months etc
For this we would need an algorithm which is able to understand the data, read, provided and make recommendations. 

# Resources Used
- [balsamiq] (https://balsamiq.com/)
- [excel] (https://github.com/alexiachm/Algorithms-project/blob/main/startups%20(4).xlsx)
- [python] (https://github.com/alexiachm/Algorithms-project/blob/main/ProjectAlgorithms.py)
- [python] (https://github.com/alexiachm/Algorithms-project/blob/main/AlgorithmsCodeStartups%20(1).py)

# Credits
This project was created for our Algorithms and Data Structures class at IE University. The authors of this project are:
- Tessa Correig
- Sofia Serantes
- Emilia Granja
- Tomas Lock
- Pilar Guerrero
- Alexia Chacon

