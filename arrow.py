import time
def draw_arrow_up(size):

    # Draw the tip of the arrow
    for i in range(1, size+1):
        print("                          "+" " * (size - i) + "*" * (2 * i - 1))

    for row in range(1,size,1):
       print("\t\t\t\t",end='')

    # Draw the bottom shaft of the arrow
    for i in range(1,size+1, 1):
        print("                          "+" " * (size - 1)+"*")

    for i in range(0,7):
       print("\t\t\t\t     *")

def draw_arrow_down(size):

    # Draw the upper shaft of the arrow
    for i in range(1,size+1, 1):
        print("                          "+" " * (size - 1)+"*")
    # Draw the tip of the arrow
    for i in range(size,0,-1):
         print("                          "+" " * (size - i) + "*" * (2 * i - 1))
    
def draw_arrow_right(size):
 
    #Draw the upper half of the arrow
    for i in range(0,(size)):
         print("                          "+" "*2*size +"*"*i + " "*2*size)

    #Draw the middle shaft of the arrow
    print("                          "+"*"*3*size)

    #Draw the lower half of the arrow
    for i in range((size-1),0,-1):
         print("                          "+" "*2*size +"*"*i + " "*2*size)

def draw_arrow_left(size):

    # Draw the top half of the arrow
    for i in range(0, (size + 2)):
        print("                          "+" " * (size-i+2) + "*" * (i - 1))

    #Draw the middle shaft of the arrow
    print("                          "+"*"*3*size)

    # Draw the bottom half of the arrow
    for i in range((size + 1), 0, -1):
        print("                          "+" " * (size-i+2) + "*" * (i - 1))

arrow_size = int(input("Enter the size of the arrow: "))

while True :
 for i in range(0,4,1):
    if i == 0:
        draw_arrow_up(arrow_size)
        time.sleep(1)
    elif i == 1:
        draw_arrow_right(arrow_size)
        time.sleep(1)
    elif i == 2:
        draw_arrow_down(arrow_size)
        time.sleep(1)
    elif i == 3:
        draw_arrow_left(arrow_size)
        time.sleep(1)