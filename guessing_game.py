import random
print("HOW TO PLAY IT")
print("STEP1:computer will generate a random number ")
print("STEP2:you have to guess within 5attempts")
print("\n")

while True:
    print("I generated succesfully.")
    random_number=random.randint(1,10)
    for i in range(1,3):
        try:
            user_input=int(input(f"Attempt{i}: Guess the number:"))
        except ValueError:
            print("enter a valid number")
            continue
        if user_input==random_number:
            print("YOU WON") 
            break
        elif i==2:
            print("YOU lost\nthe number is ",random_number) 
        elif user_input<random_number:
            print("too low,try again\n")
        else:
            print("too high,try again\n") 
    play_again=input("Do you want to play again yes/no: ") 
    if play_again=="no":
        print("thanks for playing") 
        break               