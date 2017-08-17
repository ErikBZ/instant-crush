Some issues i had with deploying django:
setting up droplet:
	none
Setting up ssh to user not root:
	Needed to create a folder in the new user .ssh and .ssh/authorized_keys
	Then needed chmod it to the new user i just created
	need to copy local ~/.ssh/id_rsa.pub into authorized_keys

	another way to do this is to create user with root and password
	set password ssh to true
	set root login to false
	repeat steps but we won't have to chmod anything

name, domaian and pointing
	
datbases:
	things weren't working for some reason. spelling mistakes and stuff fucking me
	over and over
	
Getting distracted
