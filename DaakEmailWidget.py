import gtk

class DaakEmailWidget(gtk.VBox):
	def __init__(self, subject, sender):
		super(DaakEmailWidget, self).__init__()
		
		subjectLabel = gtk.Label(subject)
		subjectLabel.show()
		senderLabel  = gtk.Label(sender)
		senderLabel.show()
		
		labelBox = gtk.VBox()
		labelBox.pack_start(subjectLabel)
		labelBox.pack_start(senderLabel)
		labelBox.show()
		
		self.pack_start(labelBox)

		deleteButton = gtk.Button('Delete')
		deleteButton.show()
		archiveButton = gtk.Button('Archive')
		archiveButton.show()
		
		buttonBox = gtk.HBox()
		buttonBox.add(deleteButton)
		buttonBox.add(archiveButton)
		buttonBox.show()
		
		self.add(buttonBox)
		self.show()
