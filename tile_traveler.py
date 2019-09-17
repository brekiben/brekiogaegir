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
    if x > 1:
        if y > 1:
            if x!=2 and y!=3:
                return True
    else:
        return False

def west(x,y):
    if x>1 and y!=1:
        if x!=3 and y!=2:
            return True

    else:
        return False

def east(x,y):
    if x !=1 and x<3:
        if x !=2 & y!=2:
            return True

    else:
        return False

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
                printsettings(x,y)
            else:
                print("Not a valid direction!")

        elif direction == "s":
            allowed = south(x,y)
            if allowed:
                y = y-1
                printsettings(x,y)
            else:
                print("Not a valid direction!")

        elif direction == "w":
            allowed = west(x,y)
            if allowed:
                x = x-1
                printsettings(x,y)
            else:
                print("Not a valid direction!")

        elif direction == "e":
            allowed = east(x,y)
            if allowed:
                x += 1
                printsettings(x,y)
            else:
                print("Not a valid direction!")

        else:
            print("Not a valid direction!")

        direction = input("Direction: ")

main()
        
        






