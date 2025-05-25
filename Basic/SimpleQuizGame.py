Question  = (
    "The biggest country in the world is ?",
    "Hotest planet in our solar system ?"
)
options = ("A :China  B:Japan  C:Russia D:Pakistan ",
           "A :Mercury  B:Venus  C:Earth D:Mars ")

correctAns = ("C","B")
option_a = 0
for i  in Question:
    print('---------------------------------------')
    print(i)
    for j in options[option_a]:
        print(j,end="")
    InputAns  = input("\nEnter your ans : ")   
    InputAns = InputAns.upper()
    if(InputAns==correctAns[option_a]):
        print("Your Answer is Correct")
    else:
        print("WRONG!")
        print("Correct Answer is : ",end="")
        print(correctAns[option_a])
    print('---------------------------------------')
    option_a +=1
    