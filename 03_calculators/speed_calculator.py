def get_name(): 
    return input("What's your name? ").strip().title() 
name = get_name()

def distance_km(): 
    return float(input("Distance in km? ").strip())
distance = distance_km() 

def time_hr(): 
    return float(input("Time in hrs? ").strip())
time = time_hr()

speed = distance / time

print(f"{name}, your speed was {speed:.2f} km/h")