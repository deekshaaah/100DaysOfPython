sen = ("Hey, My name is {} and I am from {}!")
name = "Deeksha"
country = "India"

print(sen.format(name, country))

# using f strings

print(f"I am {name} and I am from {country}!")

# f strings on numbers

amt = 39.9999
mon = f"The price of bag is {amt: .2f} dollars!"
print(mon)
print(type(mon))
