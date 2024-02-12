# kaun banega crorepati!

name = input("Enter your name : ")
print("Hey!", name, ". Are you ready to play KBC?")
print("Lets start!")

sc = 0

print("NOTE!!! : Enter the word in the exact way, i.e uppercase/lowercase")
print("GoodLuck!")

li = ["Which animal is known as the 'Ship of the Desert?", "How many days are there in a week?", "How many hours are there in a day?", "How many letters are there in the English alphabet?", "Rainbow consist of how many colours?"]


print(li[0])
print("""1. Goat
2. Camel
3. Lion
4. Panther""")
ans1 = input("Enter your answer here : ")
if ans1 == "Camel":
    print("Congratulations! Your answer is correct! :)")
    sc = 1000
else:
    print("Oops! You've lost. :(")

print(li[1])
print("""1. 25 days
2. 5 days
3. 13 days
4. 7 days""")
ans2 = input("Enter your answer here : ")
if ans2 == "7 days":
    print("Congratulations! Your answer is correct! :)")
    sc = 2000
else:
    print("Oops! You've lost. :(")

print(li[2])
print("""1. 24 hours
2. 54 hours
3. 13 hours
4. 7 hours""")
ans3 = input("Enter your answer here : ")
if ans3 == "24 hours":
    print("Congratulations! Your answer is correct! :)")
    sc = 3000
else:
    print("Oops! You've lost. :(")

print(li[3])
print("""1. 25 
2. 5 
3. 26 
4. 7 """)
ans4 = input("Enter your answer here : ")
if ans4 == "26":
    print("Congratulations! Your answer is correct! :)")
    sc = 4000
else:
    print("Oops! You've lost. :(")

print(li[4])
print("""1. 2
2. 5 
3. 13
4. 7 """)
ans5 = input("Enter your answer here : ")
if ans5 == "7":
    print("Congratulations! Your answer is correct! :)")
    sc = 5000
else:
    print("Oops! You've lost. :(")

if sc == 5000:
    print("You are the winner of KBC, we would love to give you cash price of $5000 as your reward!")
else:
    print("Better luck next time, you lost KBC!")


    



    
