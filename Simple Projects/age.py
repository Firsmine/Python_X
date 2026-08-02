from datetime import date
print("Check how old are you!")

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

try:
    year = int(input("Enter your birth year (YYYY): "))
    month = int(input("Enter your birth month (MM): "))
    day = int(input("Enter your birth day (DD): "))

    birth_date = date(year, month, day)
    age = calculate_age(birth_date)
    print(f"You are {age} years old!")

except ValueError:
    print("Invalid date format. Please enter valid numbers for year, month, and day.")
except Exception as e:
    print(f"An error occurred: {e}")