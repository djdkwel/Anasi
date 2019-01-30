def findMinWeeks(x, a, b):
    week = 0
    c=1
    bossPay=0
    anasiPay=0
    while(1):
        bossPay+=x
        x+=a
        anasiPay+=c
        c*=b
        week+=1
        if(bossPay<anasiPay):
            break
    return week
