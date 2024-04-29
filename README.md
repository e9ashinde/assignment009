### Assignment

#### Notes:
1. Store all the programs/scripts in directory `scripts`
2. All the results generated after running each of these scripts should get stored in directory `results`.
The final dircetory structure should look like
```
├── README.md
├── results
├── scripts
└── test_data
```


- Task1: Age Calculator
    1. Take `Date of Birth` as an input from user.
    2. Calulate and display the current age based on `Date of Birth`.
- Task2: Dates in different timezones
    1. Take a list of timezones as an input from the user.
    2. Display current time in each of those timezones.
- Task3: File organization
    1. Take a directory path as an input from user.
    2. Based on the filetype(file extension), organize the files in different subdirectories.
    3. Print structure of this directory.
- Task4: Size of directories
    1. Take a directory path as an input from user.
    2. Find and display size of all subdirectories on this path.
- Task5: Generate random data
    1. Write a python program to generate json data randomly.
    2. The program should create any number of json files between 12-17 and store these in test_data folder. 
    3. Each of these files should have a minimum of 1000 and maximum 39480 records.
    4. Each record should have the following keys : name, age, bio, gender
- Task6: Combine and store json
    1. Combine the data from all the files in test_data.
    2. Store it in a file named "combined_data.json"
    3. Sort the data in this file based on the key "name".
    4. Store the sorted results in file "sorted_data.json"
- Task7: 
1. Create a directory structure as shown below.
```
├── get_month.py
├── get_no_of_days.py
└── sub_dir1
    └── sub_dir2
        └── display_days.py
```
2. get_month.py
    1. Given a date as input, this file should return the month from this date.
3. get_no_of_days.py
    1. Given a month, this file should return number of days in that month. 
*`Note: Consider leap year as well.`*
4. display_days.py
    1. The script `display_days.py` should take a date as an input from user
    2. The date should be a string with format "YYYY/MM/DD"
    3. Display the number of days in the month obtained from the given date
