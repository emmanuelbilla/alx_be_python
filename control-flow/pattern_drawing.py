pattern_size = int(input("Enter the size of the pattern: "))
row_height = pattern_size

while row_height != 0:
    row_height= row_height-1
    for character in range(1, pattern_size+1):
        print("*", end="")
    print()


        
        