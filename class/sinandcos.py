# Adjacent = 5
# Opposite = 12
# Hypotenuse = ?
# hypotenuse = root(5^2+12^2)  = root(25 + 144) = root(169) = 13

import math

Adjacent = float(input("Enter the value"))
Opposite = float(input("Enter the value"))

hypotenuse = math.hypot(Adjacent, Opposite)

sin_theta =  Opposite/ hypotenuse
cos_theta = Adjacent / hypotenuse
tan_theta = Opposite / Adjacent

print("input vale(Adjacent,Opposite):")
print("hypotenuse =", hypotenuse)
print("sin(θ) =", round(sin_theta, 3))
print("cos(θ) =", round(cos_theta, 3))
print("tan(θ) =", round(tan_theta, 3))

print("sin(θ) =", round(sin_theta))
print("cos(θ) =", round(cos_theta))
print("tan(θ) =", round(tan_theta))
