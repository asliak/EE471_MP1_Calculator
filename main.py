from custom_classes import Calculator

calc = Calculator()

step1 = calc.add(10, 5)
step2 = calc.multiply(step1, 2)
step3 = calc.divide(step2, 3)

print(f"Result: {step3}")
print(f"{calc._current_val}")
