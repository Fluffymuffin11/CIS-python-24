#Ask the user for the average speed, speed limit and distance travelled.

#Calculate the amount of time saved for the distance travelled.

#THE TIME SAVED SHOULD BE REPORTED IN MINUTES

#user inputs 
average_speed = int(input("Enter your average speed in miles per hour: "))
speed_limit = int(input("Enter the speed limit posted:"))
travel_distance = int(input("Enter the miles travelled:"))

#calculate the time taken to travel at speed vs at the speed limit
time_at_average_speed = travel_distance / average_speed
time_at_speed_limit = travel_distance / speed_limit

#find time saved
time_saved =time_at_speed_limit - time_at_average_speed

#convert to mins

time_saved_minutes = time_saved * 60

#print results

if time_saved_minutes > 0:
    print("The time saved by traveling above the speed limit is {:.2f} minutes" .format(time_saved_minutes))
else:
    print("You didnt save any tome by traveling over the speed limit ")    

input("press enter to exit!")    
