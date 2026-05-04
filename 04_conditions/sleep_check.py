name = input("What's your name? ").strip().title() 
sleeping_hours = int(input("How many hours did you sleep? ")) 
def sleeping_assessment(): 
    if sleeping_hours >= 8:
        print(f"Good job, {name}!") 
    else: 
        print(f"You need more sleep, {name}!")
sleeping_assessment()