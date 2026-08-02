print("Body Mass Index Calculator")
print("Enter your weight (Kg) and your height (m^2) here\n")

def index(bmi):
    if bmi <= 18.5:
        return 'Underweight'
    elif bmi <= 25:
        return 'Normal'
    elif bmi <= 30:
        return 'Overweight'
    elif bmi > 30:
        return 'Obese'

def main():
    weight = float(input("Weight: "))
    height = float(input("Height: "))
    bmi = (weight / height**2)
    result = index(bmi)

    print(f"You're {result}")

if __name__ == "__main__":
    main()