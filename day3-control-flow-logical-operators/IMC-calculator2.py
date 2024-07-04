height = input("Qual a sua altura? ")
weight = input("Qual o seu peso? ")

height = float(height)
weight = int(weight)

imc = (weight / (height ** 2))

if imc < 18.5:
    print(f"Your BMI is {imc}, you are underweight.")
elif imc > 18.5 and imc < 25:
    print(f"Your BMI is {imc}, you have a normal weight.")
elif imc >= 25 and imc < 30:
    print(f"Your BMI is {imc}, you are slightly overweight.")
elif imc >= 30 and imc < 35:
    print(f"Your BMI is {imc}, you are obese.")
else:
    print(f"Your BMI is {imc}, you are clinically obsese.")