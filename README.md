# PROJECT OVERVIEW  

## • Problem & Solution: 
Nowadays, people don't know where their money goes each month. They spend money on food, transport, shopping, and entertainment without tracking it. This is a problem that even I encounter, hence, I’ve decided to build a personal expense tracker to document my expenses.

## • Algorithm: 

#### 1. Create list “expenses” to store all expense records. 

#### 2. Display the main menu options: 
 o Add Expense
 
 o View All Expenses 
 
 o Search Expense 
 
 o Delete Expense 
 
 o Calculate Total Spending
 
 o Display Spending by Category 
 
 o Show Highest Expense 
 
 o Save Data 
 
 o Exit 
 
#### 3. Ask the user to enter their choice. 

#### 4. If the user selects Add Expense: 
 o Ask for the date. 
 
 o Ask for the expense category. 
 
 o Ask for a short description. 
 
 o Ask for the expense amount. 
 
 o Store the entered information in a dictionary. 
 
 o Add the dictionary to the expenses list. 
 
 o Display a success message. 
 
#### 5. If the user selects View All Expenses: 
 o Check whether the expenses list is empty. 
 
 o If it is empty, display "No expenses found." 
 
 o Otherwise, display every expense with its date, category, description, and amount. 

#### 6. If the user selects Search Expense:
 o Ask the user to enter a category or keyword. 

 o Search through the expenses list. 
 
 o Display all matching expenses. 
 
 o If no matching expense is found, display an appropriate message. 

#### 7.If the user selects Delete Expense: 
 o Display all expenses with a serial number. 
 
 o Ask the user to enter the number of the expense they want to delete. 
 
 o Remove the selected expense from the list. 
 
 o Display a confirmation message. 

#### 8. If the user selects Calculate Total Spending: 
 o Set a variable named total to zero. 
 
 o Loop through every expense in the list. 
 
 o Add each expense amount to total. 
 
 o Display the total amount spent. 

#### 9. If the user selects Spending by Category: 
 o Create an empty dictionary to store category totals. 
 
 o Loop through every expense. 
 
 o Add each expense amount to its corresponding category. 
 
 o Display the total spending for every category. 

#### 10.If the user selects Highest Expense: 
 o Check whether any expenses exist. 
 
 o Compare all expense amounts. 
 
 o Find the expense with the largest amount. 
 
 o Display its date, category, description, and amount. 

#### 11.If the user selects Save Data: 
 o Save the expenses list to a file (such as a JSON file). 
 
 o Display a message confirming that the data has been saved. 

#### 12. If the user selects Exit: 
 o Save the expense data (optional). 
 
 o Display a thank-you message. 
 
 o End the program. 

#### 13. If the user selects any option other than Exit, return to the main menu and continue running the program until the user chooses to exit.

## • Visualization (Using Pseudocode):

// Main-Console

DECLARE Choice : INTEGER

Choice ← 0

WHILE Choice <> 9

    CALL DisplayMenu

    INPUT Choice

    IF Choice = 1 THEN
        CALL AddExpense
    ENDIF

    IF Choice = 2 THEN
        CALL ViewExpenses
    ENDIF

    IF Choice = 3 THEN
        CALL SearchExpense
    ENDIF

    IF Choice = 4 THEN
        CALL DeleteExpense
    ENDIF

    IF Choice = 5 THEN
        CALL CalculateTotal
    ENDIF

    IF Choice = 6 THEN
        CALL CategorySummary
    ENDIF

    IF Choice = 7 THEN
        CALL HighestExpense
    ENDIF

    IF Choice = 8 THEN
        CALL SaveData
    ENDIF

    IF Choice = 9 THEN
        OUTPUT "Thank you for using Personal Expense Tracker."
    ENDIF

ENDWHILE

// Procedure For Displaying The Main-Menu

PROCEDURE DisplayMenu

    OUTPUT " PERSONAL EXPENSE TRACKER "
    OUTPUT "1. Add Expense"
    OUTPUT "2. View Expenses"
    OUTPUT "3. Search Expense"
    OUTPUT "4. Delete Expense"
    OUTPUT "5. Calculate Total Spending"
    OUTPUT "6. Spending by Category"
    OUTPUT "7. Highest Expense"
    OUTPUT "8. Save Data"
    OUTPUT "9. Exit"

ENDPROCEDURE

// Procedure For Adding Expenses

PROCEDURE AddExpense

    Count ← Count + 1

    INPUT Date[Count]
    INPUT Category[Count]
    INPUT Description[Count]
    INPUT Amount[Count]

    OUTPUT "Expense Added Successfully."

ENDPROCEDURE

// Procedure For Viewing Expenses

PROCEDURE ViewExpenses

    IF Count = 0 THEN

        OUTPUT "No Expenses Found."

    ELSE

        FOR Index ← 1 TO Count

            OUTPUT Date[Index]
            OUTPUT Category[Index]
            OUTPUT Description[Index]
            OUTPUT Amount[Index]

        NEXT Index

    ENDIF

ENDPROCEDURE

// Procedure For Searching Expenses

PROCEDURE SearchExpense

    DECLARE SearchCategory : STRING

    INPUT SearchCategory

    FOR Index ← 1 TO Count

        IF Category[Index] = SearchCategory THEN

            OUTPUT Date[Index]
            OUTPUT Category[Index]
            OUTPUT Description[Index]
            OUTPUT Amount[Index]

        ENDIF

    NEXT Index

ENDPROCEDURE

// Procedure For Deleting Expenses

PROCEDURE DeleteExpense

    DECLARE DeleteNumber : INTEGER

    INPUT DeleteNumber

    FOR Index ← DeleteNumber TO Count - 1

        Date[Index] ← Date[Index + 1]
        Category[Index] ← Category[Index + 1]
        Description[Index] ← Description[Index + 1]
        Amount[Index] ← Amount[Index + 1]

    NEXT Index

    Count ← Count - 1

    OUTPUT "Expense Deleted."

ENDPROCEDURE

// Procedure For Calculating Total

PROCEDURE CalculateTotal

    DECLARE Total : REAL

    Total ← 0

    FOR Index ← 1 TO Count

        Total ← Total + Amount[Index]

    NEXT Index

    OUTPUT "Total Spending = ", Total

ENDPROCEDURE

// Procedure For Category Summary * not actual category-calculation logic *

PROCEDURE CategorySummary

    OUTPUT "Display total spending for each category."

ENDPROCEDURE

// Procedure To Determine The Highest Expense

PROCEDURE HighestExpense

    IF Count > 0 THEN

        Highest ← Amount[1]
        HighestIndex ← 1

        FOR Index ← 2 TO Count

            IF Amount[Index] > Highest THEN

                Highest ← Amount[Index]
                HighestIndex ← Index

            ENDIF

        NEXT Index

        OUTPUT Date[HighestIndex]
        OUTPUT Category[HighestIndex]
        OUTPUT Description[HighestIndex]
        OUTPUT Amount[HighestIndex]

    ELSE

        OUTPUT "No Expenses Found."

    ENDIF  

ENDPROCEDURE

// Procedure To Save Data

PROCEDURE SaveData
          
    OUTPUT "Data Saved Successfully."

ENDPROCEDURE

// End Of Program.

## • Libraries and Program Structures Used in the ACTUAL PYTHON PROGRAM:


####  - Libraries Used :-

The program was developed using Python's built-in features. No external libraries were required for the core functionality, however, json & os libraries were used. The program relies on Python's built-in functions such as input(), print(), len(), and range().


####  - Program Structure :-

The program is divided into small, reusable functions, making the code easier to understand & maintain.
The main functions are:

	display_menu() – Displays the main menu options.
	add_expense() – Collects expense details and stores them.
	view_expenses() – Displays all saved expenses.
	search_expense() – Searches expenses by category or description.
	delete_expense() – Removes a selected expense.
	calculate_total() – Calculates the total amount spent.
	category_summary() – Displays total spending for each category.
	highest_expense() – Finds and displays the largest expense.
	save_data() – Saves expense records to a JSON file.
	load_data() – Loads saved expense records when the program starts.
	main() – Controls the program by displaying the menu and calling the appropriate functions. 


####  - Data Structures Used :-

The program stores all expenses in a list.
Each expense is represented as a dictionary containing the following information:
	~ Date
	~ Category
	~ Description
	~ Amount

This combination of a list and dictionary allows the program to store multiple expense records efficiently while keeping each record organized and easy to access.



#### Why The Following Structures Were Chosen: 

These structures were chosen because they make the program easy to understand & maintain. 
Using functions avoids repeating code.
The list and dictionary data structures provide an efficient way to store and retrieve expense information.





# • Issues, Mistakes & Strategies Implemented to Overcome Them:


## ~ Issue 1: Translating Pseudocode into Python

	Issue: Although I had already written the pseudocode, I found it difficult to convert some parts into 	Python, especially loops and functions.

	Strategy Used: I referred to my class notes, and chatgpt, and tested each function one at a time until it 	worked correctly.

	What I Would Do Differently: I would implement AI and copy code into the AI to troubleshoot the errors 	rather than trying to figure it out on my own as it will save quite a lot of time.

## ~ Issue 2: Working with Lists and Dictionaries

	Issue: I understood the idea in the pseudocode, but I was confused about how to store and access the 	expense information using lists and dictionaries in Python.

	Strategy Used: I experimented with small examples and printed the data after each step to make sure it was 	being stored correctly.

	What I Would Do Differently: I would spend more time practicing data structures before starting the 	project.

## ~ Issue 3: Fixing Errors

	Issue: I encountered several syntax errors and indentation errors while writing the program.

	Strategy Used: I carefully read the error messages, checked the line numbers, and corrected the mistakes 	one by one.

	What I Would Do Differently: I would run the program after completing each function instead of writing 	many lines of code before testing.

## ~ Issue 4: Testing the Program

	Issue: Some menu options worked individually, but I found that moving between different options sometimes 	caused unexpected problems.

	Strategy Used: I tested every menu option several times using different inputs until the program behaved 	as expected.

	What I Would Do Differently: I would create a checklist of test cases before starting testing so I could 	verify every feature.
 


### Q. What things are you the most proud of?

~ I am most proud that I was able to complete a working program from start to finish. Before this project, I had only written small Python programs. This project helped me combine different concepts like functions, loops, lists, and dictionaries into one application. I am also happy that the program allows users to add, view, search, and delete expenses through a simple menu.

### Q. Do you think users will find these useful?

~ Yes, I think users will find this application useful because it helps them keep track of their daily expenses in one place. Instead of remembering how much they have spent, they can easily record their expenses and calculate their total spending. Although the application is simple, it solves a real-life problem.

### Q. What features have you missed out here?

~ Due to my current level of programming knowledge and the project deadline, I was not able to add every feature I wanted. For example, the application does not display graphs or charts, allow users to edit existing expenses, or include a login system for different users. These features would make the application more professional.

### Q. What steps would you take to improve this?

~ If I had more time, I would add an option to edit expenses instead of only deleting them. I would also improve the appearance of the menu, add better input validation, and include graphs to help users understand their spending habits.

### Q. Do you think this is a good fit for a website?

~ Yes, I think this project would work well as a website. A web version would allow users to access their expense records from any device with an internet connection. It would also make the application more user-friendly by providing buttons, forms, and charts instead of a text-based interface. I think converting this project into a website would be a good next step.

### Q. What are your key learnings from this entire experience?

~ This project helped me understand how to plan and build a complete Python application. I learned how to use functions to organize my code, lists and dictionaries to store data, and loops and conditions to control the program. I also learned that testing the program regularly and reading error messages carefully are important for finding and fixing mistakes. Overall, this project increased my confidence in writing Python programs and gave me a better understanding of how software is developed.
