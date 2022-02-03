def gather_info():
    height = float(input("Your height: "))
    weight= float(input("your weight: "))
    system = input("Are your measurements in metric or imperial units? ".lower().strip())
    return(height, weight, system)
def calculate_bmi(weight, height, system='metric'):
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi
while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight, system=system, height=height)
        print(f"Your BMI is {bmi}")
        if bmi < 18:
            print("Your BMI is" + str(bmi) + ". You are underweight You need food!")
        elif bmi > 18 and bmi <= 24:
            print("Your BMI is " + str(bmi) + ". You are in good shape keep it up")
        elif bmi > 25:
            print("Your BMI is " + str(bmi) + ". You are overweight you need to stop eating ")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, system=system, height=height)
        print(f"Your BMI is {bmi}")
        if bmi < 18:
            print("Your BMI is" + str(bmi) + ". You are underweight You need food!")
        elif bmi > 18 and bmi <= 24:
            print("Your BMI is " + str(bmi) + ". You are in good shape keep it up")
        elif bmi > 25:
            print("Your BMI is " + str(bmi) + ". You are overweight you need to stop eating ")
        break
    else:
        print("error")







