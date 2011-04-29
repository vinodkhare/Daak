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
		self.gmailClient.login('login', 'pass')
		
		self.prefsWindow = DaakPrefsWindow()
		self.prefsWindow.initWidgets()
    
		# Make connections
		self.indicator.prefsMenuItem.connect('activate', self.prefsWindow.presentWindow)
		self.indicator.checkMenuItem.connect('activate', self.checkNow)
		
		#Check and add timer
		self.checkNow()
		gobject.timeout_add(INTERVAL, self.checkNow)
	
	def checkNow(self, widget = None):
		print "Checking now", datetime.now()
		
		nUnread = self.gmailClient.getUnreadCount()
		self.indicator.set_label(str(nUnread))
		
		subjectList = self.gmailClient.getUnreadHeaderField('subject')
		fromList = self.gmailClient.getUnreadHeaderField('from')
		self.indicator.refreshMenu(subjectList, fromList)
		return True
		
	#~ def timeNow(self, widget):
		#~ gobject.timeout_add(5000, self.checkNow)
	
	def main(self):
		daakKeyring = Keyring('daak', 'gmail.com', 'imap')
		print daakKeyring.has_credentials()
	
		gtk.main()
