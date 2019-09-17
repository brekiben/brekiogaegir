#Create array function that creates an array with position x,y
#Create check functions for checking left, right, up down
#Create print function that prints result if check functions are true of false

def the_strings(x, y):
    str1 = "000"
    str2 = "000"
    str3 = "000"
    array = [0, str1, str2, str3]
    breyta = array[x]
    new_str= ""
    for i in range(3):
        if i == y:
            new_str +="1"
        else:
            new_str +="0"
    array[i] = new_str

    return array

def legal_moves(array):
    

    def main():
        position_x = 1
        position_y = 1