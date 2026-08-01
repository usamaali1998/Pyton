#default arguments= a default value for certain parameters defualt is used when tat arguments is omitted make your funtions more flexible , reduces # of arguments
# 1. positional, 2 . default , 3.keyword, 4. arbitrary

'''
def net_price(list_price, discount =0, tax=0.05):
    return list_price * (1-discount) * (1+tax)
print(net_price(500,20,40))
'''




