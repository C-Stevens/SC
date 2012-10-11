#SC.py - Secure Copy.py

*Written by Colin Stevens*

----

##Introduction

SC is a small, lightweight, yet powerful python script to securely transfer and copy files
between Linux-based machines and Windows environments.

The script is designed to be as user friendly as possible by using a config file, so no
manual editing of sc.py should be necessary, unless you wish to write in your own custom
features.

##Things to note

 * This script requires PSCP to run! it can be obtained [here] (http://the.earth.li/~sgtatham/putty/latest/x86/pscp.exe)

####The configuration file (conf.py):

 * Remember to fill out the configuration file for SC, and to rename it as "conf.py" (no quotes).
 * The conf.template.py file comes with arbitrary values in order to give you an idea of the proper syntax that is expected
 * Make sure to NOT wrap your numerical value for the 'waitTime' value in quotes, this will cause it to not function.
 * **Variables**
  * *PSCPdir* - Full directory path to pscp.exe on your machine.
  * *downloadDir* - Directory path on your machine where you want grabbed files to download to. If left to default value of <code>None </code>, SC.py will prompt you asking you what directory you want grabbed files to download to. Keep this value at <code>None</code> if you want to specify the download directory each time you grab files. An example of a fixed <code>downloadDir</code> value would be: <code>downloadDir=r'D:\Networking\GrabbedFiles\' </code>.
  * *user* - The user you are logging in as remotely.
  * *host* - The host that you are connecting to remotely.
  * *waitTime* - Time (in seconds) that the script will wait before auto-closing upon successful or unsuccessful file transfer or grab. Do not wrap this numerical values in quotes!

**sc.py:**

* The script is designed for there to be no need for a user to ever have to open or edit this file, as all the variables are located in the configuration file. The only
reason this file should be modified is if you wish to add your own customization to the script.

##Final Notes

All bugs, errors, suggestions, improvements, feedback, etc. are desired! You can reach me via
email at colinstevens123 at gmail dot com

You're free to modify/improve this script in any way you wish. If you have, I'd love to see
what you've done with it, and would appreciate it if you sent me an email about it.
