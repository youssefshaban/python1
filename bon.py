import random

f=open('Data.txt', 'r')
file_data=f.read()
if file_data:
    file_data=file_data.split(',')
    win=int(file_data[0])
    losse=int(file_data[1])
    if win>losse:
        message = "will seems like we have a hero here !!! \nyour score is\nWin: " + str(win) + "\nLosse: " + str(losse)
    else :
        message = "not bad for little girl ! \nyour score is\nWin: " + str(win) + "\nLosse: " + str(losse)


else:
    win=0
    losse=0
    message="welcome\n"

tries=0
entered_guesses=[]
f.close()
number=random.randrange(1,100,1)

print(message)
while tries < 10:
    inpt=input("guess a number\n")
    if inpt.isnumeric():
        inpt=int(inpt)
        if inpt>100 or inpt<1:
            print("Please input a number from 1 to 100")
        elif inpt in entered_guesses:
            print("You have already entered this guess")
        elif inpt == number:
            print("WoOoOoOoW!!!.....Congradulations! you guess right.\n")
            win+=1
            tries+=1
            entered_guesses.clear()
            number=random.randrange(1,100,1)
        elif inpt > number:
            print("number is smaller\n")
            entered_guesses.append(inpt)
            tries+=1
        elif inpt<number:
            print("Number is bigger\n")
            entered_guesses.append(inpt)
            tries+=1
    else:
        print("Entery invalid! Please Enter in the range to 100")
print("Oooops !!! not bad for a little girl ...\nyou were not able to guess the number which is:",number)
losse+=1
f=open('Data.txt', 'w')
f.write(str(win)+","+str(losse))
f.close()