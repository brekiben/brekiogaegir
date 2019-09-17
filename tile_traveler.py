#Create array function that creates an array with position x,y
#Create check functions for checking left, right, up down
#Create print function that prints result if check functions are true of false

def north(x,y):
    if x==1 or x== 3:
        if y < 3:
            return True

    elif x==2 and y==1:
        return True

    else:
        return False

def south(x,y):
    true_false = True
    if y <=1:
        true_false = False
    if x ==2 and y==3:
        true_false = False

    return true_false

def west(x,y):
    true_false = True
    if x <=1:
        true_false = False

    if x==3 and y ==2:
        true_false = False
    if x==3 and y ==1:
        true_false = False
    if x ==2 and y ==1:
        true_false = False
    return true_false

def east(x,y):
    true_false = True
    if x >= 3:
        truefalse = False
    if x == 1 and y ==1:
        true_false = False
    if x==2 and y ==2:
        true_false = False
    if x==2 and y==1:
        true_false = False
    
    return true_false

def checkvictory(x,y):
    if x ==3 and y==1:
        return True
    else:
        return False

def printsettings(x,y):
    print("You can travel:", end =" ")
    if x==1 or x==2 or x==3:
        if y ==1:
            print("(N)orth.")
    if x==1 and y==2:
        print("(S)outh or (E)ast or (N)orth.")
    if x ==2 and y==2:
        print("(S)outh or (W)est.")
    if x ==3 and y ==2:
        print("(N)orth or (S)outh")
    if x ==1 and y ==3:
        print("(S)outh or (E)ast")
    if x==2 and y==3:
        print("(E)ast or (W)est.")
    if x==3 and y==3:
        print("(S)outh or (W)est")


def main():
    x = 1
    y = 1
    victory = checkvictory(x, y)
    printsettings(x,y)
    direction = input("Direction: ")
    while victory != True:
        direction = direction.lower()

        if direction == "n":
            allowed = north(x,y)
            if allowed:
                y += 1
                victory = checkvictory(x,y)
                if victory:
                    break
                else:
                    printsettings(x,y)
            else:
                print("Not a valid direction!")

        elif direction == "s":
            allowed = south(x,y)
            if allowed:
                y = y-1
                victory = checkvictory(x,y)
                if victory:
                    break
                else:
                    printsettings(x,y)
            else:
                print("Not a valid direction!")

        elif direction == "w":
            allowed = west(x,y)
            if allowed:
                x = x-1
                victory = checkvictory(x,y)
                if victory:
                    break
                else:
                    printsettings(x,y)
            else:
                print("Not a valid direction!")

        elif direction == "e":
            allowed = east(x,y)
            if allowed:
                x += 1
                victory = checkvictory(x,y)
                if victory:
                    break
                else:
                    printsettings(x,y)
            else:
                print("Not a valid direction!")

        else:
            print("Not a valid direction!")


        
        direction = input("Direction: ")
        
main()
print("Victory")
        
        






