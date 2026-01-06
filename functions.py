#define math functions
def add(a, b):
    return a + b
def diff(a, b):
    return a - b
def multiply(a, b):
    return a * b
def div(a, b):
    return a / b

#Greets user with given name, defaults to guest    
def say_greet(name='Guest'):
    print(f'Hello, {name}!')
#generic dictionary function
def add_or_update(data, key, value):
    data[key] = value
def reomve_key(data, key):
    return data.pop(key, None) is not None
#specific for contact list or inventory    
def add_contact(contacts, name, phone):
    contacts[name] = phone    
def remove_contact(contacts, name):
    if name in contacts(contacts, name):
        contacts.remove(name)
    else:    
        print('contact not found')    
def add_inventory(inventory, item, qty):
    inventory[item] = qty  
def remove_inventory(inventory, item):
    if item in inventory(inventory, item):
        inventory.remove(item)
    else:    
       print('Item not found')     

#function for expense calc
def get_expns(budget_dict, category_name):
    for category, amount in budget_dict['expenses']:
        if category == category_name: 
            return amount
    return None      
def add_expns(budget_dict, category_name, amount):
    budget_dict['expense'].append((category_name, amount))
def update_expens(budget_dict, category_name, new_amount):
    for i, (category, amount) in enumerate(budget_dict['expenses']):
            if category == category_name: 
                budget_dict['expenses'][i] = (category, new_amount)
                return
    add_expns(budget_dict, category_name, new_amount)  
