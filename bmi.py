def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = ", weight)

    BMI = weight / (height ** 2)
    print("BMI = ", f"{BMI: .2f}")

    if BMI < 18.5:
        print("underweight")
    elif BMI >= 25:
        print("overweight")
    else:
        print("normal weight")


    for x in range(5):
        print("6 7")

calculate_bmi(weight=67, height=1.73)
calculate_bmi(1.60, 10)
calculate_bmi(1.82, weight=85)