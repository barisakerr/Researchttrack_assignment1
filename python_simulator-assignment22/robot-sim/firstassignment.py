from __future__ import print_function

import time
from sr.robot import *

a_th = 2.0 # fload: Threshold for the control of the orientation
d_th = 0.4 # float: Threshold for the control of the linear distance

golden_trashhold = 0.65 # the maximum distance between the robot and the golden token, for releasing the silver token
silver_trashhold = 0.45 # the maximum distance between the robot and the silver token, for grabing the silver token

silver = True

R = Robot()

offset_G = [] # Array of the golden tokens' offsets 
offset_S = [] # Array of the silver tokens' offsets 

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
    """
    Function to find the closest silver token

    Returns:
	dist (float): distance of the closest silver token (-1 if no silver token is detected)
	rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
    """
    dist=100 # possible maximum distance for the robot to see the token
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER: # condition for seeing the token; if the distance between the robot and the token is less than possible maximum distance which is 'dist=100' and  if the marker type of the token is silver
            dist=token.dist 
	    rot_y=token.rot_y
	    offset = token.info.offset # offset to understand the which token that the robot will grab
    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, offset

def find_golden_token():
    """
    Function to find the closest golden token

    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
    """
    dist=100 # possible maximum distance for the robot to see the token
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD: # condition for seeing the token; if the distance between the robot and the token is less than possible maximum distance which is 'dist=100' and  if the marker type of the token is golden
            dist=token.dist
	    rot_y=token.rot_y
	    offset = token.info.offset # offset to understand the which token that the robot will be released to 
    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, offset

while 1:
    if silver == True: # if silver is True, then the robot starts to look for a silver token, otherwise robot will start to look for a golden one
	dist, rot_y, offset = find_silver_token()
	
	if offset in offset_S: # if the token which is the robot is seeing, is already in the array then robot turns 
		turn(30,0.1) # robot turns on the right to find another token
	
	elif dist==-1: # if no token is detected, the robot turns 
		print("I don't see any token!!")
		turn(+10, 1)
        elif dist < silver_trashhold: # if the distance between the robot and the token is less than the maximum possible grabbing distance, it means robot is close enough to the token to grab it
        	print("Found it!") 
        	
        	if R.grab(): # the robots grabs the token
          		print("Gotcha!") # after grabbing the token prints("Gotcha!") to inform the user     		
	    		turn(-20, 1.8) # robot turns on the left 	    		    			
	    		offset_S.append(offset) # offset of the silver token which has been grabbed by the robot is adding to the array of the silver tokens' offsets 
	    		print(offset_S) # printing the array of the silver tokens' offsets
			silver = not silver # we modify the value of the variable silver, so that in the next step we will look for the other type of token (golden token)
	        else:
           		print("Aww, I'm not close enough.")
   
   	elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
		print("Ah, that'll do.")
        	drive(50, 0.2) # robot going to forward
    	elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
        	print("Left a bit...")
        	turn(-2, 0.5) # robot turns on the left 
    	elif rot_y > a_th:
        	print("Right a bit...")
        	turn(+2, 0.5) # robot turns on the right

    else: # silver becomes false (silver == False) and the robot starts to look for the golden tokens
	dist, rot_y, offset = find_golden_token()
    
    	if offset in offset_G: # if the token which is the robot is seeing, is already in the array 
		turn(30,0.1) # robot turns on the right to find another token
			
	elif dist==-1: # if no token is detected, we make the robot turn to find another token
		print("I don't see any token!!")
		turn(+10, 1) #robot turns on the right 
        elif dist < golden_trashhold: # if the distance between the robot and the token is less than the maximum possible realising distance, it means robot is close enough to the token to release the grabbed token
        	print("Found it!")
        	
        	if R.release(): # the robots release the grabbed token near to the golden token 
          		print("Released!") # after releasing silver token to the golden token the code printing 'release' to inform the user
          		drive(-20,1) #robot going to back 
	    		turn(20, 1.9) # robot turns on the right
	    		drive(20,2) # robot going to forward
	    		offset_G.append(offset) # offset of the golden token is adding to the array of the golden tokens' offsets 
	    		print(offset_G) # printing the array of the golden tokens' offsets
			silver = not silver # we modify the value of the variable silver, so that in the next step we will look for the other type of token
	        else:
           		print("Aww, I'm not close enough.")
   
   	elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
		print("Ah, that'll do.")
        	drive(30, 0.2) # robot going to forward
    	elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
        	print("Left a bit...")
        	turn(-2, 0.5) # robot turns on the left 
    	elif rot_y > a_th:
        	print("Right a bit...")
        	turn(+2, 0.5) # robot turns on the right
     	    
    if len(offset_G) == 6 and len(offset_S) == 6: # when the length of the golden and the silver tokens' offset's array become six, the code stops working
    	print("All Done!") #  user will be inform about the code is finished by printing the "All Done!"
    	exit() # code stop working and robot will stop

	
    
