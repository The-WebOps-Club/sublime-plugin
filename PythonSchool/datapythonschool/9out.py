#### OUTPUT START ####
name = raw_input("Hi user,Please enter your name: ")
if len(name)>7:
	print("Hey %s, Your name is way too lengthy") % (name)
elif len(name)<7:
	print("Hey %s, Your name is way too small") % (name)
else:
	print("Hey %s, Your name is perfect") % (name)
#### OUTPUT END ####