#nested loop = A loop within another loop(outer, inner)
#       outer loop:
    #       inner loop:


rows = int(input("Enter the # of rows"))
col = int(input("Enter the # of col"))
symbol = input("Enter the symbol to use")



for x in range(rows):
    for y in range(col):
        print(symbol,end="")
    print()
