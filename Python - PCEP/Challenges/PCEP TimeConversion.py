#The objective of this challenge is for the student to convert time after 
#The user input hour then minutes (HH:MM) + minutes in duration (MM)
#The code should get that data and output the final HH:MM
#Limitations: Allowed usage of 
#Type Casting
#Aritmetic Operations
#Not Allowed: Control Structures of any sort either condition or count-controlled.
#Total Time I took to do this with control structures: 15 minutes
#Time took to complete this challenge under above conditions: 2 hours
#Aligned with PCEP-30-02 Module 2

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

#Calculate event duration in hours and minutes
durationsHours = dura // 60
durationsMins = dura % 60
exceedsAnHour = (dura + mins) // 60

#Calculate the final times for hours and minutes
hourFinal =(hour + exceedsAnHour) % 24
minsFinal = (durationsMins + mins) % 60

#Display the result using seg and : to 
print(hourFinal,minsFinal,sep=":")