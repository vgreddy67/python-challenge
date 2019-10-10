# python-challenge
Python-Challenge has 2 different challenges in it. PyBank and PyPoll. PyBank we analzye the financial records of a company.
	PyPoll we try to modernize a small rural communities vote counting process.
	Doing this project as a tarining project to learn data analysis using Python.
  
  python-challenge has 2 parts : PyBank and PyPoll
  
  PyBank:
 
 PyBank has 3 files in it : budget_data.csv , main.py and budget_output.txt
  
 budget_data.csv file has a companies dataset that contains two columns : Date and profit/losses 
 main.py file has python code to analyze the data from the csv file.
      Description of variables in the python code:
        budget_csv - Stores the file path for the csv file
        output - Stores the file path for the budget_output.txt file
        budgetreader - reader handle for the csv file of the csv file
        count - used to keep track of the total number of months in the file
        totalAmount - the net total amount of the profit/losses column
        prevRow - used to store the profit/losses of the previous row.
                  (This is done by assiging it the current row value after all the manipulations)
        increaseDate - defined this as a string variable(as we don't have any manipulations with this variable).
                       Used this to find the date on which there was a maximum increase in profits
        decreaseDate - defined this as a string variable (as we don't have any manipulations with this varaible).
                       Used this to find the date on which there is a maximum decrease in the profits or maximum losses.
        maxProfitIncrease - Stores the greatest  profit increase
        maxProfitDecrease - Stores the greatest decrease in profits
