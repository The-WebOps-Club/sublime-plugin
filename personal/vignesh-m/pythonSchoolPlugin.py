import sublime, sublimeplugin

class pythonSchoolCommand:
	def run(self,view,args):
		Window curr=view.window()
		View newf=curr.newfile()
		newf.insert(0,"Text")