#this is a game that tells us whether the input number is odd or even
def oddeven(n):
    n = int(n)
    if n % 2 ==0:
        print(n, " is an even number")
    else:
        print(n, " is an odd number")
    print("Thanks for playing!")

def user():
    global s 
    s= input("Tell us any number that you can think of!\n")
    print(oddeven(s))
print(user())

f=1
while f>0:
    f = int(input("Would you like to play again? Type \"1\" if yes and \"0\" if no."))
    if f==1:
        print("Hope you enjoy the game once more!")
        print(user())
    elif f == 0: 
        print("Alright, thanks for playing!")
        break;
    else: 
        print("Sorry we do not accept that answer.")
        break;
