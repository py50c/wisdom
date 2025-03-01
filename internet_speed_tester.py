import speedtest
import time
print("Loading..." , end= '\r')
time.sleep(2)
print("Almost done..." , end = '\r')
time.sleep(3)

#user Direction/instruction
print(f"""Hello there it's good to know you're using my internet connection speed test tool.""")
time.sleep(5)
print("""\nThis program has been thoroughly designed to calculate your internet connection speed either at a particular time or the average. Kindly follow the instructions to carefully to use the program.""")
time.sleep(8)
print("\n	press 'C' to continue" )
C = input().lower()

#checking that user input meets program requirement
while C != "c":
	print("Invalid user input! Please try again\nPress 'C' to continue")
	C = input().lower()
else:
	pass
	
#further instruction
print("""\nYou can either calculate your speed just at a particular time (once) or calculate the average speed for more accuracy.

To calculate ONCE, press 'O'
To calculate AVERAGE speed, press 'A'\n""")
choice = input().lower()

#checking user's input
ch = ["o" , "a"]
while choice  not in ch:
	print("Invalid user input! Please try again\nTo calculate ONCE, press 'O'\nTo calculate AVERAGE speed, press 'A'\n")
	choice = input().lower()
else:
	pass

if choice == "o":
	print("Please wait..." , end = '\r')
	time.sleep(2)
	print("Connecting to server..." , end = '\r')
	time.sleep(3)
	try:
		st = Speedtest() #creating an intance of the Speedtest class inside the speedtest module. This class contains the method (function) that will calculate the speed.
		st.get_best_server() #finding best server to determine speed
	except Exception as e:
		print(""""ooh ooh! an error was encountered while connecting to server.Please check your internet connection and try again.""") # printed if server connection is not successful.
	else: #this block is executed when try block is executed
		print("succesfully connected to server!" , end = '\r') #printed if server conection is siccessful.
		time.sleep(1)
		print("sending request to calculate speed..." , end = '\r')
		time.sleep(2)
		print("Calculating download speed...                   " , end = '\r')
		download = st.download()/1000000 #calculates and stores download speed in megabits per second
		time.sleep(3)
		print("Calculating upload speed...                 		 " , end = '\r')
		upload = st.upload()/1000000#Calculates and stores upload speed in megabits per second
		time.sleep(2)
		print("Processing results...                                     " , end = "\r")
		time.sleep(3)
		
		#speedtest result
		print(f"""                SPEED TEST RESULT:     
                ==================
        Download speed: - {round(download, 2)}Mbps
        Upload speed: - {round(upload, 2)}Mbps""") # rounds result to 2dp
        
        
        #final note
		print("\nThat's your speed result. Thanks for using my tool!\nTo calculate again, please restart program.")
		
		
else: # if user opts for average speed
	print("Select number of times for the calculation\n(choose from 1 - 4 )")
	choice = (input()) #allows user specify number of times for soeed to be calculated
	list = ["1","2","3","4"] #stores allowed users input
	while choice not in list: # loop continue while users choice is invalid i.e not in list
		print("invalid input! Plese try again.\n choose from 1 - 4")
		choice = (input()) #takes new user input
	Nchoice = int(choice) #converts users choice to an integer value
	try:
		print("please wait...            ", end = '\r')
		time.sleep(2)
		print("Connecting to server...       " , end = '\r')
		st = Speedtest() #creating an intance of the Speedtest class inside the speedtest module. This class contains the method (function) that will calculate the speed.
		st.get_best_server() #finding best server to determine speed
	except Exception as e:
			print(""""ooh ooh! an error was encountered while connecting to server.Please check your internet connection and try again.""") # printed if server connection is not successful.
	else:
		print("succesfully connected to server!      " , end = '\r') #printed if server conection is siccessful.
		time.sleep(1)
		print("sending request to calculate speed..." , end = '\r')
		
	# iterating over user input to calculate speed
		count = 0 #initializes count value
		download_list = [] #empty list that will store collected download speed for calculating its average
		upload_list = [] #empty list for collecting upload speed to calculate its average
		for i in range(0, Nchoice):	#loooping the no. of times of user input
			print(f"Calculating download speed...(round {count+1})                   " , end = '\r')
			download = st.download()/1000000 #calculates and stores download speed in megabits per second
			download_list.append(download)#appends speed value to the download list
			time.sleep(3)
			print(f"Calculating upload speed... (round {count+1})                 		 " , end = '\r')
			time.sleep(2)
			upload = st.upload()/1000000#Calculates and stores upload speed in megabits per second
			upload_list.append(upload)#appends upload speed value to the upload list
			print(f"round {count+1} speed succesfully calculated.                                              ")
			count+=1
		time.sleep(1)
		print("Compiling results...              " , end = '\r')
		time.sleep(2)
		avDownload = round((sum(download_list)/len(download_list)) , 2) # calculates average download speed and rounds to 2dp
	
		avUpload = round((sum(upload_list)/len(upload_list)) , 2) #calculates average download speed and rounds to 2dp
	
		print(f"""                SPEED TEST RESULT:     
                ==================
        Average download speed: - {avDownload}Mbps
        Average upload speed: - {avUpload}Mbps""") #speed test result
        
        
        #final note
		print("\nThat's your speed result. Thanks for using my tool!\nTo calculate again, please restart program.")
