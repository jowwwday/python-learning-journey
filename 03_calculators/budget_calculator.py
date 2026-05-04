# Budget Calculator
# Converted from Jupyter Notebook

def get_name(): 
    return input("What's your name? ").strip().title() 


def get_money():
    return float(input("How much money do you have? "))


def get_days_before_paycheck():
    return int(input("How many days until salary? ")) 


def calculate_daily_budget(money, days): 
    return money / days 


def print_result(name, daily_budget):
    print(f"{name}, you can spend {daily_budget:.2f} per day.")


def give_advice(daily_budget): 
    if daily_budget > 3000:
        print("You are living comfortably.")
    elif daily_budget >= 1000:
        print("Your budget is moderate.") 
    else:
        print("You should save money.")


name = get_name() 


money = get_money() 


days = get_days_before_paycheck()


if days == 0: 
    print("Days cannot be zero.") 
else:
    daily_budget = calculate_daily_budget(money, days) 
    print_result(name, daily_budget) 
    give_advice(daily_budget) 

