asa-capture
===========
This is a simple script that logs into a specific test ASA and saves 'show version' to a local file.

**There's more information on installation and learning prerequisites on the wiki:**
https://netprog.atlassian.net/wiki/pages/viewpage.action?pageId=1736800

The idea is we can use this script to start learning python and linux and then expand upon this script to start doing more useful things. This script will be built up to capture packet captures from CLI or web GUI eventually.

These are some good pages to get started learning some of the specific things used in this script.
pexpect:
* http://www.pythonforbeginners.com/systems-programming/how-to-use-the-pexpect-module-in-python
* http://pexpect.sourceforge.net/pexpect.html#-run
* http://pexpect.readthedocs.org/en/latest/install.html

* Expect scripts: http://en.wikipedia.org/wiki/Expect

As well, the basic python information on: modules, files, stdin/stdout, print, variable types, comments, and sys

More advanced:
* Help figure out whether pexpect, paramiko, or exscript is the best module to interact with SSH and the ASA
* Start figuring out how to interactively parse and display packet information to the command line
* If this gets ported to a web GUI, what framework would make sense for displaying this information
* We'll need to pull down the packet capture - what's the best method (looks like https). We'll need urllib and other tools to pull that capture. What errors will we run into?
* Is there a way to display wireshark in the browser?
* What about real-time display of packet information in the browser?
