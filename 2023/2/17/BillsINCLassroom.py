area = 57.33 #Note Change as needed
#      _____
height = 3 #Note Change as needed
#        _
def calc(billspermeter, area, h, valueperbill):
	return h*area*billspermeter*valueperbill
print(calc((1000 / 120) * (1000 / 62) * (8333 + 1 / 3), area, height, 719.28))
#                                                                     ______  
print("Amount of bills you can fit in one meter: " + str((1000 / 120) * (1000 / 62) * (8333 + 1 / 3)))
