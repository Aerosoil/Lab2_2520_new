def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = ", weight)

    BMI = weight / (height ** 2)
    print("BMI = ", f"{BMI: .2f}")

    if BMI < 18.5:
        print("underweight")
        return -1
    elif BMI >= 25:
        print("overweight")
        return 1
    else:
        print("normal weight")
        return 0

    for x in range(5):
        print("6 7")

print(calculate_bmi(weight=67, height=1.73))
calculate_bmi(1.60, 10)
calculate_bmi(1.82, weight=85)