
![SqlPuzzle](sql_puzzle.jpg)



# Project SQL Data Base Building 
# Data Cleaning with Jupyter Notebook and Data Base Building SQL with MySQL Work 


# Overview
It aims to demonstrate how to preprocess and clean raw data, and then store the cleaned data in a relational database for further analysis. The project includes a Jupyter Notebook that contains data cleaning procedures and SQL with MySQL Work queries for creating and populating the database tables.
Client has supplied the project with 7 data frames as CVS files from his old Rental Film Shop.

# Data Cleaning Process
-	Juptyter Notebook, libraries Numpy, Pandas, Matplotlib and Seaborn
-	Overall data analysis comprehension: head, shape, info, unique values, duplicate, column titles
-	Major changes: column drops: ‘last_update’, ‘original_language_id’
-	Minor changes: column reorder, column rename, reset upper and lowercase, date format adjustment. 
-	Old data and Clean data are saved as .cvs files inside folder data
-	Cleaning process are saved as .py files inside folder scc or as .ipynb inside folder notebooks 

# SQL Database Setup
-	MySQL Workbench
-	Creation of new data base scheme: retro_dvd_vhs
-	Creation of tables titles as equal as in cleaned .cvs files. 
-	Exceptions 1: HDD file was not used; it may be selected as query since has no unique data.
-	Data Seeding accomplished by using Table Data Import Wizard command.
-	Exception 2: Language has a new proposal of table:  up to date to the film industry globalization. Data Seeding accomplished by Alter Table command.
-	Creation of 3 new tables to complete data base structure: Staff, Store and Customers. Data Seeding accomplished by Alter Table command.
-	Definition of one-to-many and many-to-many relations in the structure. Diagram image is saved as .png file inside folder queries.
-	Database creation and seeding are saved as .sql files inside folder queries.

# Enquiry
-	Five enquiries were done to increase comprehension on the database structure.
-	Main learnings: There are 207 films in inventory, however, it appears that all those titles start only with letter A to D. Hypothesis is that old Inventory file was given incomplete or corrupted. 
-	Queries codes are saved as .sql files and theirs output are saved as .xlx file inside queries folder.
