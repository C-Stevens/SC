from timedExit import timedExit
#Compatibility for older versions of python
try: 
	raw_input
except NameError:
	raw_input = input
try:
	import configparser as ConfigParser
except ImportError:
	import ConfigParser
config = ConfigParser.ConfigParser()

#Group script into function for calls in SC
def buildConf():
	print('Refer to the README for a description and examples of each variable.')
	#Create sections and define variable pairs
	config.add_section('Directories')

	while True:
		selection = raw_input('Do you want a static download directory? ').lower()
		if selection in  ('yes', 'y'):
			downloadDir = raw_input('Directory path on your machine where you want grabbed files to download to: ')
			config.set('Directories', 'downloadDir', downloadDir)
			break
		elif selection in ('no', 'n'):
			config.set('Directories', 'downloadDir', 'None')
			print('No static download directory set. SC will ask you for a download directory upon each run')
			break
		else:
			print('[!] Invalid response. Supported responses are: yes, y, no, n (case insensitive)')

	while True:
		selection = raw_input('Do you want a static trasnfer directory? ').lower()
		if selection in ('yes', 'y'):
			fileDir = raw_input('Directory path on your machine where you willt transfer all files from: ')
			config.set('Directories', 'fileDir', fileDir)
			break
		elif selection in ('no', 'n'):
			config.set('Directories', fileDir, 'None')
			print('No static transfer directory set. SC will ask you from what location you want to transfer files upon each run')
			break
		else:
			print('[!] Invalid response. Supported responses are: yes, y, no, no (case insensitive)')

	config.add_section('Login')

	sshUser = raw_input('The user you will be logging in as: ')
	config.set('Login', 'User', sshUser)
	sshHost = raw_input('The host you will be connecting to: ')
	config.set('Login', 'Host', sshHost)

	config.add_section('Misc')

	#while loop to ensure value entered is an integer
	while True:
		waitTime = raw_input('Amount of time (in seconds) that the script will wait before auto-closing: ')
		if not waitTime.isdigit():
			print('[!] Invalid entry. Only integers may be used for wait time.')
		else:
			config.set('Misc', 'waitTime', waitTime)
			break

	#Write config file
	with open('conf.cfg', 'w') as configfile:
		config.write(configfile)
		print('Config written successfully! \n')

#Have script run itself if run seperate from SC
if __name__ == '__main__':
	buildConf()
	timedExit(None, 6, 1)
