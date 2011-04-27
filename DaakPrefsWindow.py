import gtk


class DaakPrefsWindow(gtk.Window):
	count = 1
	visible = False

	def toggleVisible(self, widget, event = 0):
		if self.visible == False:
			self.show()
			self.present()
			self.visible = True
		else:
			self.hide()
			self.visible = False

	def presentWindow(self, widget):
		self.present()

	def initWidgets(self):
		self.usernameLabel = gtk.Label('User name: ')
		self.usernameLabel.show()
		
		self.usernameEntry = gtk.Entry()
		self.usernameEntry.show()
		
		self.usernameBox = gtk.HBox(False, 0)
		self.usernameBox.pack_start(self.usernameLabel)
		self.usernameBox.pack_start(self.usernameEntry)
		self.usernameBox.show()
		
		self.passwordLabel = gtk.Label('Password: ')
		self.passwordLabel.show()
		
		self.passwordEntry = gtk.Entry()
		self.passwordEntry.set_visibility(False)
		self.passwordEntry.show()
		
		self.passwordBox = gtk.HBox(False, 0)
		self.passwordBox.pack_start(self.passwordLabel)
		self.passwordBox.pack_start(self.passwordEntry)
		self.passwordBox.show()
		
		self.winBox = gtk.VBox(False, 0)
		self.winBox.pack_start(self.usernameBox)
		self.winBox.pack_start(self.passwordBox)
		self.winBox.show()
		
		self.add(self.winBox)
		self.connect('delete-event', self.hide_on_delete)
