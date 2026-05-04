def get_name():
   return input("What's your name? ").strip().title()

name = get_name()

def get_age():
   return int(input("What's your age? ").strip())

age = get_age()

def age_in_10_years(age):
    print(f"In ten years you will be {age + 10}")

age_in_10_years(age)