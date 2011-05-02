from email.header import decode_header

import appindicator
import gtk

class DaakIndicator(appindicator.Indicator):
	def initWidgets(self):
		self.set_status(appindicator.STATUS_ACTIVE)
		self.menu = gtk.Menu()
		self.addPermanentMenuItems()

	### Adds the permanent menu items.		
	def addPermanentMenuItems(self):
		self.quitMenuItem = gtk.MenuItem('Quit')
		self.quitMenuItem.show()
		self.quitMenuItem.connect("activate", gtk.main_quit)
		
		self.prefsMenuItem = gtk.MenuItem('Preferences')
		self.prefsMenuItem.show()
		# prefsMenuItem.connect("activate", prefsWindow.toggleVisible)
		
		self.checkMenuItem = gtk.MenuItem('Check Now')
		self.checkMenuItem.show()
		
		#~ self.timeMenuItem = gtk.MenuItem('Time')
		#~ self.timeMenuItem.show()
		
		self.menu.append(self.checkMenuItem)
		#~ menu.append(self.timeMenuItem)
		self.menu.append(self.prefsMenuItem)
		self.menu.append(self.quitMenuItem)

		self.set_menu(self.menu)
		

	def refreshMenu(self, subjectList, fromList):
		# Remove the existing menu items
		for i in self.menu.get_children():
			self.menu.remove(i)
			
		nUnread = len(subjectList)
		
		if nUnread == 0:
			item = gtk.MenuItem('No unread messages')
			item.show()
			item.set_sensitive(False)
			self.menu.prepend(item)
			
		for i in range(nUnread):
			subject = unicode(decode_header(subjectList[i])[0][0])
			item = gtk.MenuItem('%s\n\t%s' % (subject, fromList[i]))
			item.show()
			self.menu.prepend(item)
		
		separator = gtk.SeparatorMenuItem()
		separator.show()
		self.menu.append(separator)
			
		self.addPermanentMenuItems()
			
		
			
		
