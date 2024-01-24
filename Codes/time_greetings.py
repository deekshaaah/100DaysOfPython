import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
print(hour)

if (hour>0 and hour<12):
    print("Good Morning Madam/Sir")
if (hour>=12 and hour<22):
    print("Good Evening Madam/Sir")
else:
    print("Good Night Madam/Sir")
