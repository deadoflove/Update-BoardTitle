#within

class BoardWithTitleBar(Board):

#search:

		titleName.SetPosition(0, 4)

#replace

		if not  app.UPDATE_BOARDTITLE:
			titleName.SetPosition(0, 4)

#search:

		self.SetCloseEvent(self.Hide)

#Add:

		if app.UPDATE_BOARDTITLE:
			self.SetTitlePosition(0, 4)

#search

	def SetTitleColor(self, color):
		self.titleName.SetPackedFontColor(color)

#Add

	if app.UPDATE_BOARDTITLE:
		def SetTitlePosition(self, x, y):
			self.titleName.SetPosition(x, y)

#within

	def LoadElementBoardWithTitleBar(self, window, value, parentWindow):

#search

		window.SetTitleName(value["title"])

#add:

		if app.UPDATE_BOARDTITLE:
			if True == value.has_key("color"):
				window.SetTitleColor(value["color"])
			if value.has_key("text_x") and value.has_key("text_y"):
				window.SetTitlePosition(int(value["text_x"]), int(value["text_y"]))




