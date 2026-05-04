name = input("What's your name? ").strip().title() 
temperature = float(input("What's your temperature? ").strip())
def temperature_check(): 
    if temperature >= 37.5: 
        print(f"{name}, you should rest at home!")
    else: 
        print(f"{name}, you seem fine.")

temperature_check()