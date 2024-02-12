# coding

print("This is a code to convert a word into a secret language!")

word = input("Enter a word to convert into a secret language : ")
count = len(str(word))
    
if count >= 3:
    letter = word[0]
    removed = word[1:]
    new_word = "yay" + removed + letter + "eww"
    print("The secret word is",new_word)
    
else:
    rev_word = word[::-1]
    print("The secret word is",rev_word)
    
#decoding

print("Now, if you wish to decode your secret word, enter 'Yes' and if not, then enter 'No'")
user_input = input("Enter 'Yes' or 'No' : ")

if user_input == 'Yes':
    decode_word = input("Enter a word : ")
    count_word = len(str(decode_word))
    
    if count_word <= 3:
        rev_decode_word = decode_word[::-1]
        print(rev_decode_word)
    
    else:
        decode = decode_word[3:-3]
        last_letter = decode[-1]
        decoded = last_letter + decode
        result = decoded[:-1]
        print(result)
        
else:
    print("No problem! Enjoy using this secret code word! :)")
