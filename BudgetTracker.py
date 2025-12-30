#function for difference 
import functions

#declare monthly income
inc = int(input('Enter your monthly income: '))
#declare dollar amount of each bill
#bills are stored in a list until user cancels  
bills = []
try: 
    while True:
        user_input = input('Enter bill amounts or q to cancel: ')
        if user_input.lower() == 'q':
            break 
        bill = int(user_input)    
        bills.append(bill)
except ValueError:
    print('Error. Enter bill amount')
    
   
#Add up all bills in list to find total amount
total_bills = sum(bills)  
print('Your total bills are $' + str(total_bills))
#find budget by calculating diff of income vs bills  
budget = functions.diff(inc, total_bills)
print('Your budget is $' + str(budget))
#user enters total of extra spending 
spending = int(input('Enter how much extra you have spent this month: '))
#find total expenses for month
exp_total = (functions.diff(budget, spending))
#informs if over budget or on track
if exp_total < 0:
    print ('Total Expenses: $' + str(exp_total))
    print('You are over budget')
else:    
    print ('Total Expenses: $' + str(exp_total))
    print('You are on track')
