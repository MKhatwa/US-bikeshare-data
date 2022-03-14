# US-bikeshare-data
A basic data exploration related to bike share systems for three major cities in USA.

## Project Overview
This project uses Pandas library in Python to perform variety descriptive analysis (e.g. most popular days or most common stations on the bikeshare data for three major cities in the United States—Chicago, New York City, and Washington.

## How to run it
Input 'python bikeshare.py' on your terminal to run this program. Anaconda's command prompt would be sufficient.

## Program Details
First, the program takes user input for the city (e.g. Chicago), month for which the user wants to view data (e.g. January; also includes an 'all' option), and day for which the user wants to view data (e.g. Monday; also includes an 'all' option).

Upon receiving the user input, it goes ahead and asks the user if they want to view the raw data (5 rows of data initially) or not.

Following the input received, the program prints the following details:

### 1 Popular times of travel (i.e., occurs most often in the start time)

A. most common month
B. most common day of week
C. most common hour of day

### 2 Popular stations and trip

A. most common start station
B. most common end station
C. most common trip from start to end (i.e., most frequent combination of start station and end station)

### 3 Trip duration

A. total travel time
B. average travel time

### 4 User info

A. counts of each user type
B. counts of each gender (only available for NYC and Chicago)
C. earliest, most recent, most common year of birth (only available for NYC and Chicago)

Finally, the user is prompted with the choice of restarting the program or not.

## Requirements
  1. Language: Python 3.6 or above
  2. Libraries: Pandas, Numpy and Time
  
## Project Data
All the csv files are stored in a zip file that is located in the data folder. Each city will have its own dataset with it's name.

## Author
[Mahmoud Abou Khatwa](https://github.com/MKhatwa)- sole author for this program.

## Acknowledgements

- [The Future of Work is Digital Initiative](https://egfwd.com/)- The egyptian FWD initiative for their opportunity that equiped me with the neccassery tools to make this project possible.
- [Udacity](https://www.udacity.com/)- Udacity's Data Analyst Proffesional Nanodegree program and their instructors were extremely helpful while I was pursuing this project.
- [pandas docs](https://pandas.pydata.org/pandas-docs/stable/)- pandas documentation was immensely helpful in understanding the implemention of pandas methods used in this project.
