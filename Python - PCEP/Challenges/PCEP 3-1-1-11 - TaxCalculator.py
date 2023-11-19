#The objective of this challenge is for the student to run a tax calculator
# 3.1.1.11 on Python Essentials
# ReadMe has the detailed requirements
# Sample values are as follows
#Test Data
#Sample Input: 10000
#Expected Output: The tax is: 1244.0 thalers
#
#Sample Input: 100000
#Expected Output: The tax is: 19470.0 thalers
#
#Sample Input: 1000
#Expected Output: The tax is: 0.0 thalers
#
#Sample Input: -100
#Expected Output: The tax is: 0.0 thalers

income = float(input("Enter the annual income: "))

if income > 85528:
    exceeding = income - 85528
    taxPercentageBase = exceeding * 0.32
    tax = 14839.02 + taxPercentageBase
    
elif income <= 85528:
    tax = (income * 0.18) - 556.02

if tax <= 0:
    tax = 0.0
    

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
