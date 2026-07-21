#1. Square Root
import math

num = 25
print(math.sqrt(num))


#2. Cube Root
num = 27
print(num ** (1/3))


#3. Factorial
import math

num = 5
print(math.factorial(num))


#4. GCD
import math

print(math.gcd(24, 36))


#5. LCM
import math

print(math.lcm(12, 18))


#6. Power (5⁸)
import math

print(math.pow(5, 8))


#7. Absolute Value
import math

print(math.fabs(-25.67))


#8. Ceiling Value
import math

print(math.ceil(5.2))


#9. Floor Value
import math

print(math.floor(5.9))


#10. Round to Nearest Integer
print(round(5.6))


#11. Remainder using math.fmod()
import math

print(math.fmod(17, 5))


#12. Quotient and Remainder using divmod()
q, r = divmod(17, 5)

print("Quotient =", q)
print("Remainder =", r)


#13. Sine, Cosine, Tangent of 45°
import math

angle = math.radians(45)

print(math.sin(angle))
print(math.cos(angle))
print(math.tan(angle))


#14. Degrees to Radians
import math

print(math.radians(90))


#15. Radians to Degrees
import math

print(math.degrees(math.pi))


#16. Log Base 10
import math

print(math.log10(100))


#17. Natural Logarithm
import math

print(math.log(10))


#18. e Raised to x
import math

print(math.exp(2))


#19. Value of π and e
import math

print("Pi =", math.pi)
print("Euler =", math.e)


#20. Distance Between Two Points
import math

point1 = (2, 3)
point2 = (6, 7)

print(math.dist(point1, point2))


#21. Hypotenuse
import math

print(math.hypot(3, 4))


#22. Combination (nCr)
import math

print(math.comb(5, 2))


#23. Permutation (nPr)
import math

print(math.perm(5, 2))


#24. Check Finite, Infinite, NaN
import math

print(math.isfinite(10))
print(math.isinf(float("inf")))
print(math.isnan(float("nan")))


#25. Product of List Elements
import math

numbers = [2, 3, 4, 5]

print(math.prod(numbers))


#26. Sum of Square Roots
import math

numbers = [4, 9, 16]

total = sum(math.sqrt(i) for i in numbers)

print(total)


#27. Largest Integer ≤ Square Root
import math

num = 30

print(math.floor(math.sqrt(num)))


#28. Compound Interest
import math

P = 10000
R = 5
T = 2

A = P * math.pow((1 + R / 100), T)

print("Amount =", A)
print("Compound Interest =", A - P)


#29. Area and Circumference of Circle
import math

r = 7

area = math.pi * r * r
circumference = 2 * math.pi * r

print("Area =", area)
print("Circumference =", circumference)


#30. Scientific Calculator
import math

print("------ Scientific Calculator ------")
print("1. Square Root")
print("2. Factorial")
print("3. Log10")
print("4. Power")
print("5. Sin")
print("6. Cos")
print("7. Tan")
print("8. GCD")
print("9. LCM")

choice = int(input("Enter your choice: "))

if choice == 1:
    num = float(input("Enter number: "))
    print("Square Root =", math.sqrt(num))

elif choice == 2:
    num = int(input("Enter number: "))
    print("Factorial =", math.factorial(num))

elif choice == 3:
    num = float(input("Enter number: "))
    print("Log10 =", math.log10(num))

elif choice == 4:
    a = float(input("Enter base: "))
    b = float(input("Enter exponent: "))
    print("Result =", math.pow(a, b))

elif choice == 5:
    angle = float(input("Enter angle in degrees: "))
    print("Sin =", math.sin(math.radians(angle)))

elif choice == 6:
    angle = float(input("Enter angle in degrees: "))
    print("Cos =", math.cos(math.radians(angle)))

elif choice == 7:
    angle = float(input("Enter angle in degrees: "))
    print("Tan =", math.tan(math.radians(angle)))

elif choice == 8:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("GCD =", math.gcd(a, b))

elif choice == 9:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("LCM =", math.lcm(a, b))

else:
    print("Invalid Choice")