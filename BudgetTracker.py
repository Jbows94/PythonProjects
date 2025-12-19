#function for difference 
def diff(a, b):
    return a - b

#declare monthly income
inc = int(input('Enter your monthly income: ')
#declare dollar amount of each bill
#bills are stored in a list until user cancels
bills = []
while True: 
    bill = int(input('Enter bills or q to cancel: ')
    if bill.lower() == q
        break
    bills.append(bill)
#Add up all bills in list to find total amount
total_bills = sum(bills)  
print('Your total bills are $' total_bills)
#find budget by calculating diff of income vs bills  
budget = diff(inc, total_bills)
print('Your budget is $' budget)
#user enters total of extra spending 
spending = int(input('Enter how much extra you have spent this month: ')
#find total expenses for month
#informs if over budget or on track
total_exp = diff(budget, spending)
if total_exp < 0:
    print ('Total Expenses: $' + str(total_exp))
    print('You are over budget')
else:    
    print ('Total Expenses: $' + str(total_exp))
    print('You are on track')
