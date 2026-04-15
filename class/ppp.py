
''''import phonenumbers
from phonenumbers import carrier  
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("9939749850", "IN")
phone_number2 = phonenumbers.parse("9693111187", "IN")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en")) '''

"""import phonenumbers
from phonenumbers import carrier


phone_number1 = phonenumbers.parse("9939749850", "IN")
phone_number2 = phonenumbers.parse("9693111187", "IN")

print("\nPhone Numbers Location\n")
print(carrier.name_for_number(phone_number1, "en"))
print(carrier.name_for_number(phone_number2, "hi"))  """


'''import phonenumbers
from phonenumbers import is_valid_number


phone_number1 = phonenumbers.parse("9939749850", "IN")
phone_number2 = phonenumbers.parse("9693111187", "IN")

print("\nPhone Numbers Location\n")
print(is_valid_number(phone_number1))
print(is_valid_number(phone_number2)) '''

import phonenumbers
from phonenumbers import is_possible_number


phone_number1 = phonenumbers.parse("9939749850", "IN")
phone_number2 = phonenumbers.parse("9693111177", "IN")

print("\nPhone Numbers Location\n")
print(is_possible_number(phone_number1))
print(is_possible_number(phone_number2))

'''from phonenumbers import *

phone = parse("9939749850", "IN")

print("Carrier:", carrier.name_for_number(phone, "en"))
print("Region:", geocoder.description_for_number(phone, "en"))
print("Valid:", is_valid_number(phone))
print("Possible:", is_possible_number(phone))
print("Type:", number_type(phone))'''

