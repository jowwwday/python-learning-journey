def get_name():
    return input("What's your name? ").strip().title()

name = get_name()

def get_bill(): 
   return float(input("What was your bill? ").strip())

bill = get_bill()

def tip_percentage(): 
   return float(input("Tip percentage? ").strip())


tip = tip_percentage()

tip_amount =  bill * tip/100

print(f"{name}, your total bill was {bill + tip_amount}")


