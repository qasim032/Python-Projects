import random
def main():
    ranNum = randomNum()
    guess = get_num(ranNum)
    print(f"You guess the number in {guess} attempts.")
    
    
def get_num(ranNum):
    guess = 0
    print("Guess the number b/w 1-100: ")
    while True:
        num = int(input())
        guess+=1
        if num>ranNum:
            print("Please guess a small number: ")
            continue
        if num<ranNum:
            print("Please guess a large number: ")
            continue
        else:
            return guess
def randomNum():
  
    return  random.randint(1, 100)
main()