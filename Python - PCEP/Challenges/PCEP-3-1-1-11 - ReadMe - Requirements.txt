Estimated Time
10-20 minutes

Difficulty Level
Easy/Medium

Objectives
To familiarize the student with:

Using the if-else statement to branch control flow.
Building a complete program to solve simple real-life problems.

Scenario
Once upon a time, there was a land—a land of milk and honey, inhabited by happy and prosperous people. People paid taxes, of course—their happiness had limits. The most important tax, called the Personal Income Tax (IRS or PIT in English), had to be paid once a year and was assessed using the following rule:

If the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was called tax relief).
If the income was higher than this amount, the tax would be equal to 14,839 thalers and 2 cents, plus 32% of the surplus above 85,528 thalers.
Your task is to write a tax calculator.

It should accept a floating-point value: the income.
Next, it should print the calculated tax, rounded to whole thalers. There is a function called round() that will do the rounding for you—you will find it in the skeleton code in the editor.
Note: This happy country never refunds money to its citizens. If the calculated tax is less than zero, it simply means that there is no tax (the tax is equal to zero). Keep this in mind during your calculations.

See the code in the editor—it reads only one input value and outputs a result, so you need to complete it with some smart calculations.

Test your code using the data provided by us.

Test Data
Sample Input: 10000

Expected Output: The tax is: 1244.0 thalers

Sample Input: 100000

Expected Output: The tax is: 19470.0 thalers

Sample Input: 1000

Expected Output: The tax is: 0.0 thalers

Sample Input: -100

Expected Output: The tax is: 0.0 thalers