import sys
from statistics import mean

# dummy params

## FUNCTIONS
# get hourly stock data from last 7 days
# get contract details for a given leg

class leg():
    def __init__(self):
        self.midPrice = 2.99

class comboContract():

    def __init__(self):

#        leg1 = leg()
#        leg2 = leg()
#        leg1.midPrice = 3
#        leg2.midPrice = 4

        self.legs = []
 #       self.legs.append(leg1)
 #       self.legs.append(leg2)


    def getMidPrice(self):
        sum=0
        for l in self.legs:
            sum += l.midPrice
        return(sum/float(len(self.legs)))

mySpread = comboContract()

leg1 = leg()
leg2 = leg()
leg3 = leg()
leg1.midPrice = 1
leg2.midPrice = 3
leg3.midPrice = 4

mySpread.legs.append(leg1)
mySpread.legs.append(leg2)
mySpread.legs.append(leg3)

print(mySpread.getMidPrice())
