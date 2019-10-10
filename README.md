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

PyPoll:
	We are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
PyPoll has two three files in it: election_data.csv, main.py and election_output.txt
	The dataset is composed of three columns: Voter ID, County, and Candidate. A Python script is created that analyzes the votes and calculates each of the following:
	The total number of votes cast:
		A complete list of candidtes who received votes.
		The percentage of votes each candidate won.
		The total number of votes each candidate won.
		The winner of the election based on popular vote.
		
Analysis looks similar to the one below:

Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
