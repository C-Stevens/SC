import subprocess
import sys
import time

def timedExit(message='', timeout=None, returnCode=0):
	if message:
		print (message)
	if timeout is None:
		timeout = conf.waitTime
	print ('Auto closing in', timeout, 'seconds...')
	time.sleep(timeout)
	sys.exit(returnCode)

try:
	import conf
except:
	timedExit('Config file missing!', 5, 1)

try:
        raw_input
except NameError:
        raw_input = input

while True:
	selection = raw_input('Transfer or Grab files? ').lower()
	
	if selection in ('transfer', 'tr', 't'):
		fileDir = raw_input('Full directory path to file to transfer: ')
		transferDir = raw_input('Full directory on host to transfer to: ')
		returncode = subprocess.call([conf.PSCPdir, '-r', fileDir, conf.user + '@' + conf.host + ':' + transferDir])
		
		if returncode == 0:
			print ('Transfer complete!')
		else:
			print ('Transfer failed')
		timedExit()
		
	elif selection in ('grab', 'gr', 'g'):
		dirName = raw_input('Directory path to file(s): ')
		fileName = raw_input('Filename (and extension) to grab: ')
		returncode = subprocess.call([conf.PSCPdir, '-r', conf.user + 	'@' + conf.host + ':' + dirName + '/' + fileName, conf.downloadDir])
		
		if returncode == 0:
			print ('Grabbing completed!')
		else:
			print ('Grab failed.')
		timedExit()
		
	else:
		print ('Invalid entry. Supported responses are Transfer or Grab (case insensitive)')
