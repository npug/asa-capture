# 2014-07-10/DN - attempting to implement argparse so that user, pwd & IP can be 
#    passed in from CLI.
# 2014-07-10/DN - Works with my ASA but I had to add an enable option as the enable pwd
#    is different. Might be nice to default the enable password to the user password if 
#    that was supplied.

import pexpect 	#module for logging into the ASA
import sys 	#module for writing files to log/linux shell
import argparse	#parsing command line arguments

# 2014-07-10/DN - debugging to clear the screen with each run
#import os		#operating system options 
#os.system('cls' if os.name == 'nt' else 'clear')

parser = argparse.ArgumentParser(description='Get "show version" from a Cisco ASA.')
parser.add_argument('-u', '--user', default='cisco', help='user name to login with (default=cisco)')
parser.add_argument('-p', '--password', default='cisco', help='password to login with (default=cisco)')
parser.add_argument('-e', '--enable', default='cisco', help='password for enable (default=cisco)')
parser.add_argument('-d', '--device', default='192.168.120.160', help='device to login to (default=192.168.120.160)')
args = parser.parse_args()

#child becomes the object to send/receive commands from the ASA
child = pexpect.spawn('ssh '+args.user+'@'+args.device)

#for debugging we send the input and output to the linux shell
child.logfile_read = sys.stdout
child.logfile_send = sys.stdout

#familiar process of logging into a cisco device
#expect waits for response from the console
#some special characters here like:
#   . means any character
#   + means the previous character 1 or more times
#   * means the previous character 0 or more times

#the print commands are here in case you run into trouble and will give you an idea where the script stopped
print 'expecting password'
child.expect('.*password: ')

print 'sending password'
child.sendline(args.password)

print 'expecting login'
#expecting the hostname> prompt
child.expect('.*> ')
child.sendline('enable')

#expecting the enable password prompt
child.expect('Password.*')
print 'sending password'
child.sendline(args.enable)

print 'expecting exec'
#expecting a login prompt of hostname#
child.expect('.*#.*')

#setting the terminal length to infinity so we don't need to press space or enter to continue the prompt
child.sendline('terminal pager 0')

#setting a new file for output so we can write output from the screen to a file for later
fout = file('test.log','w')
child.expect('.*#.*')

#setting the show version output to a file
child.logfile_read = fout
child.sendline('show version')

#expecting the hostname# prompt
child.expect('.*#.*')
fout.close()  #closing the file for best practice
child.sendline('exit')	# logout of the ASA
exit()

