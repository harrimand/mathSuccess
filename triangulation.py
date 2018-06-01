# Triangulation System

import math

LT = 40
RT = 60

Width = 48 * 2.54  # Area Width = 48 inches -> centimeters

LTr = LT * math.pi / 180    #Convert to Radians
RTr = RT * math.pi / 180

LTslope = math.tan(LTr) #Tangent = opposite/adjacent = rise/run = slope
RTslope = -1 * math.tan(RTr)
print("-" * 79)
print("\nUse Tangent of LT and RT angles to obtain slopes\n")
print("Left Slope = tan({:0.2f} deg)".format(LT))
print("Left Slope :  {:0.3f}".format(LTslope))

print("\nRight Slope = -1 * tan({:0.2f} deg)".format(RT))
print("Right Slope: {:0.3f}".format(RTslope))

print("-" * 79)
print("\nGiven Area Width: {:0.2f} centimeters.".format(Width))

print("-" * 79)
print("\nCalculate Y Intercepts for both lines\n")
print("Left Y Intercept = 0")
print("Right Line Y Intercept = -1 * Area_Width * RT_Line_slope")
print(" -1 * {:0.2f} * {:0.2f} = {:0.2f}".format(Width, RTslope, Width * -RTslope))
LTyInt = 0
RTyInt = Width * -RTslope

print("\nLT Y intercept: {:0.2f} centimeters.".format(LTyInt))
print("RT Y intercept: {:0.2f} centimeters.".format(RTyInt))
print("-" * 79)

print("\nWrite Functions for Line L(X) and R(X)")
print("Standard Line function:  Y = mX + b\n")
Lx = (" {:0.2f} * X + {:0.2f}".format(LTslope, LTyInt))
Rx = ("{:0.2f} * X + {:0.2f}".format(RTslope, RTyInt))

print("L(x) =  ", Lx)
print("R(x) = ", Rx)

print("-" * 79)
print("\nSolve for X where L(x) = R(x)\n")
print(Lx + "  =  " + Rx)

print(" {:0.2f} X + {:0.2f} X = {:0.2f}".format(LTslope, -RTslope, RTyInt))
print(" {:0.2f} X = {:0.2f}".format(LTslope - RTslope, RTyInt))
print(" X = {:0.2f} / {:0.2f}".format(RTyInt, LTslope - RTslope))
X = RTyInt / (LTslope - RTslope)
print(" X = {:0.2f}".format(X))
print("-" * 79)

print("\nPlug X into either equation to solve for Y\n")
Y_LT = LTslope * X + LTyInt
Y_RT = RTslope * X + RTyInt
Y = Y_LT
print(" Y_LT(X) =  {:0.2f} * {:0.2f} +  {:0.2f} = {:0.2f}".format(LTslope, X, LTyInt, Y_LT))
print(" Y_RT(X) = {:0.2f} * {:0.2f} + {:0.2f} = {:0.2f}".format(RTslope, X, RTyInt, Y_RT))
print(" Y = {:0.2f}".format(Y))
print("-" * 79)

print("\nSolution:  X = {:0.2f}\t Y = {:0.2f}".format(X, Y_LT))

