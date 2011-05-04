from datetime import *

import gtk
import gobject

from DaakIndicator import *
from DaakPrefsWindow import *
from pygmail import *
from keyring import *

INTERVAL = 60000

class DaakApplication:
	def __init__(self):
		self.indicator = DaakIndicator("daak", "/home/vinod/Code/Daak/daak-new.png", appindicator.CATEGORY_APPLICATION_STATUS)
		self.indicator.initWidgets()
	
		self.gmailClient = pygmail()
		login, password = self.getLogin()
		self.gmailClient.login(login, password)
		
		self.prefsWindow = DaakPrefsWindow()
		self.prefsWindow.initWidgets()
    
		# Make connections
		self.indicator.prefsMenuItem.connect('activate', self.prefsWindow.presentWindow)
		self.indicator.checkMenuItem.connect('activate', self.checkNow)
		
		#Check and add timer
		self.checkNow()
		gobject.timeout_add(INTERVAL, self.checkNow)
	
	def checkNow(self, widget = None):
		nUnread = self.gmailClient.getUnreadCount()
		self.indicator.set_label(str(nUnread))
		
		subjectList = self.gmailClient.getUnreadHeaderField('subject')
		fromList = self.gmailClient.getUnreadHeaderField('from')
		
		print "Checking now", datetime.now(), type(nUnread)
		
		self.indicator.refreshMenu(subjectList, fromList)
		return True
		
	#~ def timeNow(self, widget):
		#~ gobject.timeout_add(5000, self.checkNow)
	
	def getLogin(self):
		inFile = open('.daakrc')
		login = inFile.readline().strip()
		password = inFile.readline().strip()
		print login, password
		return (login, password)
	
	def main(self):
		daakKeyring = Keyring('daak', 'gmail.com', 'imap')
		print daakKeyring.has_credentials()
	
		gtk.main()
