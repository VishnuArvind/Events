print("      Welcome To Hangman Game    ")
print()
word=str(input("Enter a word: "))
print("The Length of the given word is",len(word))
lword=word.lower()
chances=5
correct=0
while(chances!=0 and correct!=len(lword)):
    a=str(input("Enter a letter: "))
    b=a.lower()
    if b in lword :
        c=word.count(b)
        print("Correct")
        correct+=c
    else:
        print("Wrong")
        chances-=1
    if chances==0 and correct!=len(word) :
        print("     Game Over")
        break
    if correct==len(lword):
        print("     You Won")
print()
if correct==len(lword):
    print("    Congratulations")
else:
    print("    Good Try..Better Luck Next Time ")
    
    
    
