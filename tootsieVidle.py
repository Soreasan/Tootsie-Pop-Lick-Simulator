import sys
import math as m
from visual import *
import random

#We don't know the constant right now, before we used 110 but now we randomly generate a value
#between 80 and 120 since tongues may have slightly different constants
constant = 80 + 40 * random.random()
print "The randomly generated constant for this run is: "
print constant,
print "seconds per kilogram"

# we measured the tootsie pops and their average radius was 0.0280 meters
initialSuckerRadius = 0.0280
suckerRadius = []
suckerRadius.append(initialSuckerRadius)
#dt or change of time is 0.5 seconds
dt = 0.5
dryFrictionalForce = 0.11417 #newtons
wetFrictionalForce = 0.01393 #newtons

#We may not need this equation
def halfVolumeOfSphere(radius):    
    return (((2 * m.pi)/3) * (radius**3))
    
#dt is aount of time per lick
def radiusOfLick(constant, frictionalForce, dt):
    return frictionalForce * dt / constant
    
def radius2(radius1, radiusOfLick):
    return radius1- radiusOfLick
    
#We are not using this equation
def volumeLostByLick(radius1, radius2):
    myConstant = ((2 * m.pi) / 3)
    return (myConstant * radius1**3 - myConstant * radius2**3)
    
def calculateNewRadius(myRadius1, constant, frictionalForce, dt):
    #Added the divide by two since we're only licking half the tootsie pop per lick.  
    myRadiusOfLick = radiusOfLick(constant, frictionalForce, dt)/2
    return radius2(myRadius1, myRadiusOfLick)

suckerRadius.append(calculateNewRadius(suckerRadius[-1], constant, dryFrictionalForce, dt))

#Creating static tootsie pop
staticTootsiePop = sphere(pos = (-(3 * initialSuckerRadius), 0, 0), color = color.red, radius = initialSuckerRadius)
staticTootsiePopHandle = box(pos=(-(3 * initialSuckerRadius), (-(initialSuckerRadius * 2.5)), 0), size=((initialSuckerRadius / 5), (initialSuckerRadius * 5), (initialSuckerRadius / 5)))
textStatic = text(text='Unlicked \ntootsie pop', align='center', depth=-(initialSuckerRadius / 8), height=initialSuckerRadius / 3, pos = (-(3 * initialSuckerRadius), (initialSuckerRadius * 3), 0),color=color.green)
staticTootsiePopCylinder = cylinder(pos=(-(initialSuckerRadius * 3),0,-(initialSuckerRadius * 0.275)), axis=(0,0,(initialSuckerRadius * 0.55)), radius=(initialSuckerRadius * 1.1), color=color.red)

#Creating licked tootsie pop
tootsiePop = sphere(pos = (0, 0, 0), color = color.orange, radius = initialSuckerRadius)
tootsiePopHandle = box(pos=(0, (-(initialSuckerRadius * 2.5)), 0), size=((initialSuckerRadius / 5), (initialSuckerRadius * 5), (initialSuckerRadius / 5)))
textLicked = text(text='Licked \ntootsie pop', align='center', depth=-(initialSuckerRadius / 8), height=initialSuckerRadius / 3, pos = (0, (initialSuckerRadius * 3), 0),color=color.green) 
lickedTootsiePopCylinder = cylinder(pos=(0,0,-(initialSuckerRadius * 0.275)), axis=(0,0,(initialSuckerRadius * 0.55)), radius=(initialSuckerRadius * 1.1), color=color.orange)
licks = 0
lickExplanation = text(text='Lick Counter:', align='center', depth=-(initialSuckerRadius / 8), height=initialSuckerRadius / 3, pos = ((initialSuckerRadius * 3), (initialSuckerRadius), 0),color=color.green)
lickCounter = text(text=str(licks), align='center', depth=-(initialSuckerRadius / 8), height=initialSuckerRadius, pos = ((initialSuckerRadius * 3), -(initialSuckerRadius/2), 0),color=color.green)
while (suckerRadius[-1] > 0):
    rate(50)
    newRadius = calculateNewRadius(suckerRadius[-1], constant, wetFrictionalForce, dt)
    tootsiePop.radius = newRadius
    lickedTootsiePopCylinder.pos = (0, 0, -(newRadius * 0.275))
    lickedTootsiePopCylinder.axis=(0,0,(newRadius * 0.55))
    lickedTootsiePopCylinder.radius=(newRadius * 1.1)
    licks += 1
    lickCounter.text=str(licks)
    suckerRadius.append(newRadius)
print "It took",
print str(licks),
print "licks to get to the center of the tootsie pop"
