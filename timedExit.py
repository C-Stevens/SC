import sys
import time
try:
	import configparser as ConfigParser
except ImportError:
	import ConfigParser

config = ConfigParser.ConfigParser()


def timedExit(message='', timeout=None, returnCode=0):
	if message:
		print (message)
	if timeout is None:
		if not config.has_option('Misc', 'waittime'):
			config.read('conf.cfg')
		timeout = config.get('Misc', 'waittime')
	print ('Auto closing in', timeout, 'seconds...')
	time.sleep(float(timeout))
	sys.exit(returnCode)
	