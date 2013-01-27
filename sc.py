import subprocess
import sys
import os
import time
from timedExit import timedExit
from buildConf import buildConf
from version import version

#Compatibility for older versions of python
try:
	import configparser as ConfigParser
except ImportError:
	import ConfigParser
config = ConfigParser.ConfigParser()
try:
	raw_input
except NameError:
	raw_input = input

print('Secure Copy - version ' + version + '\n')

#Check for config, build if necessary
config.read('conf.cfg')
if not config.has_section('Directories'):
	print ('[!] Config file malformed or missing.')
	while True:
		buildSelection = raw_input(' Would you like to run buildConf now to create a new config? ').lower()
		if buildSelection in ('yes', 'y'):
			print(' running buildConf.py...')
			buildConf()
			config.read('conf.cfg')
			from timedExit import timedExit
			break
		elif buildSelection in ('no', 'n'):
			timedExit('[!] Config file failed to load! Verify state and integrity of the file!', 7, 1)
		else:
			print(' Unsupported response. Supported responses are: yes, y, no, n [case insensitive]')
else:
	print ('Config loaded successfully!')

#redefine all config variables for easier calling
PSCP = 'PSCP.exe'
downloadDir = config.get('Directories', 'downloaddir')
fileDir = config.get('Directories', 'fileDir')
user =  config.get('Login', 'user')
host =  config.get('Login', 'host')

while True:
	selection = raw_input('Transfer or Grab files? ').lower()
	
	if selection in ('transfer', 'tr', 't'):
		if fileDir == 'None':
			fileDir = raw_input('[!] Static transfer directory not specified in config file.\n Full directory path to transfer files from: ')
		elif not fileDir.endswith(os.sep):
			fileDir += os.sep

		while True:
			transFile = raw_input('File you want to transfer [wildcards accepted]: ')
			transferDir = raw_input('Full directory on host to transfer to: ')
					
			if subprocess.call([PSCP, '-r', fileDir+transFile, user + '@' + host + ':' + transferDir]):
				print ('[!] Transfer failed')
			else:
				print ('Transfer complete!')
			transferAgain = raw_input('Would you like to start another transfer? ').lower()
			if transferAgain in ('no', 'n'):
				timedExit()
		
	elif selection in ('grab', 'gr', 'g'):
		#Various checks to download directory to ensure script can continue
		if downloadDir == 'None':
			downloadDir = raw_input('[!] Download directory not specified in config file.\n Full directory path to download files to: ')
		elif not downloadDir.endswith(os.sep):
			downloadDir += os.sep

		while True:
			dirName = raw_input('Directory path to file(s): ')
			fileName = raw_input('File with extension to grab [wildcards accepted]: ')

			if subprocess.call([PSCP, '-r', user + '@' + host + ':' + dirName + fileName, downloadDir]):
				print ('[!] Grab failed.')
			else:
				print ('Grabbing completed!')
			grabAgain = raw_input('Would you like to start another grab? ').lower()
			if grabAgain in ('no', 'n'):
				timedExit()
		
	else:
		print ('[!] Invalid entry. Supported responses are Transfer or Grab (case insensitive)')
