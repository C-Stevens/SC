#SC - Secure Copy
*Written by Colin Stevens*

----

##Introduction

SC is a small, lightweight, yet powerful python script to securely transfer and copy files
between Linux-based machines and Windows environments.

The script is designed to be as user friendly as possible by using a config file, so no
manual editing of sc.py should be necessary, unless you wish to write in your own custom
features.

##Things to note

 * This script requires PSCP to run! By default, it is included in the SC package, however if it needs to be re-obtained or you wish for more information about the program, you can visit the author's website <a href="http://www.chiark.greenend.org.uk/~sgtatham/putty/">here</a>.
 * SC does not currently have the capability to ssh auth with public/private key pairs. Instead, you can only grab/transfer into servers through password-based authentication.

##Included with SC
Following is a list of all files that should be included in the SC package with a description of each file's purpose.
#####The configuration build file (buildConf.py):

 * This file is used for generating the SC configuration file, which holds all of the needed variables and values required to make grabs/transfers
 * If no configuration file is present when SC is run, or the configuration file is malformed, SC will prompt you if you want to build a new <code>conf.cfg</code> file. Therefore, you should never have to run this script manually unless you wish to change values to an intact <code>conf.cfg</code> file after the first build inside SC.
 * For reference when building or manually editing the configuration file, refer to this set of variables for information:
  * <code>downloadDir</code> - The directory path on your machine to which grabbed files will download to. If set to <code>None</code>, SC will ask you where you want to download files to each time you run the program.
  * <code>fileDir</code> - The directory path on your machine from which you will transfer files out of.  If set to <code>None</code>, SC will ask you from where you want to transfer files each time you run the program.
  * <code>user</code> - The user you will be logging in as on the remote machine.
  * <code>host</code> - the host you will be connecting to for grabs/transfers.
  * <code>waitTime</code> - the amount of time (in seconds) that the script will use by default when auto-exiting.

#####The example configuration file (example.cfg)
* Included with SC is a pre-made example of an already built configuration file. Any config files built from buildConf (whether run individually or through SC) should look very similar in structure.
* The example configuration file gives you an idea of the proper syntax and nature of each variable with an example.

#####Licensing information (LICENSE)
* Contains only the licensing information for both SC and the license for PuTTy/PSCP in full.

##### PSCP (PSCP.exe)
* Included with SC is PSCP.exe, the main component of the script. It's through this program that SC formulates the grab/transfer calls.
* If for some reason you don't have PSCP included with your SC package, or need to re-acquire it for any other reason, it can be obtained directly through <a href="the.earth.li/%7Esgtatham/putty/latest/x86/pscp.exe">this</a> link.

##### SC (sc.py)
* sc.py is the main script that does all of the grabbing/transfer functions. **This is the file that should be run when you want to make grabs/transfers**
* This file is designed so that it should never need to be edited manually to make it function. The only reason you would need to edit this file would be to add your own functionality to it.

##### Timed exit script (timedExit.py)
* This script is called by SC whenever it executes an auto-exit of the program.
* The timing before the program closes is imported from the configuration file, however there are few instances inside SC where the timing is static and will not reflect the value in the configuration file. For example, when the conf.cfg file fails to load, the timing is set at a static time of 7 seconds.

##### Program version (version.py)
* Includes the current version of SC to be printed upon running the program

##Final Notes

All bugs, errors, suggestions, improvements, feedback, etc. can be forwarded to be via email at colinstevens123(at)gmail(dot)com

Current version - 2.0.0
