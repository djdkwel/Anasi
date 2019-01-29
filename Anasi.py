"""def findMinWeeks(x, a, b):
    count = 0
    c=1
    totalA=x
    totalB=1
    while totalA>totalB:
        c*=b
        totalB+=c
        count+=1
        print(totalA)
        print(totalB)
    return count """
def findMinWeeks(x, a, b):
    count = 0
    c=1
    totalA=0
    totalB=0
    while totalA>=totalB:
        totalA+=x
        x+=a
        totalB+=c
        c*=b
        #totalB+=c
        count+=1
        print(totalA)
        print(totalB)
    return count
