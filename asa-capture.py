import pexpect #module for logging into the ASA
import sys #module for writing files to log/linux shell

#child becomes the object to send/receive commands from the ASA
child = pexpect.spawn('ssh cisco@192.168.120.160')

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
child.expect('cisco.+: ')
print 'sending password'
child.sendline('cisco')
print 'expecting login'
#expecting the hostname> prompt
child.expect('.*> ')
child.sendline('enable')
#expecting a password prompt
child.expect('Password.*')
print 'sending password'
child.sendline('cisco')
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
child.expect('.*#.*')
fout.close()  #closing the file for best practice
child.sendline('exit')
exit()

