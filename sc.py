import subprocess
import sys
import time
try:
	import conf
except:
	print ('Config file missing!')
	print ('Auto closing in 5 seconds...')
	time.sleep(5)
	sys.exit(1)

try:
        raw_input
except NameError:
        raw_input = input

while True:
	selection = raw_input('Transfer or Grab files? ')
	
	if selection in ['Transfer']:
		fileDir = raw_input('Full directory path to file to transfer: ')
		transferDir = raw_input('Full directory on host to transfer to: ')
		returncode = subprocess.call([conf.PSCPdir, '-r', fileDir, conf.user + '@' + conf.host + ':' + transferDir])
		
		if returncode == 0:
			print ('Transfer complete!')
		else:
			print ('Transfer failed')
		print ('Auto-closing in {0.waitTime} seconds...'.format(conf))
		time.sleep(conf.waitTime)
		break
		
	elif selection in ['Grab']:
		dirName = raw_input('Directory path to file(s): ')
		fileName = raw_input('Filename (and extension) to grab: ')
		returncode = subprocess.call([conf.PSCPdir, '-r', conf.user + 	'@' + conf.host + ':' + dirName + '/' + fileName, conf.downloadDir])
		
		if returncode == 0:
			print ('Grabbing completed!')
		else:
			print ('Grab failed.')
		print ('Auto-closing in {0.waitTime} seconds...'.format(conf))
		time.sleep(conf.waitTime)
		break
		
	else:
		print ('Invalid entry. Supported responses are Transfer or Grab (case sensitive)')
