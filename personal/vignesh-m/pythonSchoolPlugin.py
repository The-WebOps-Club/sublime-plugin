import sublime, sublime_plugin ,os ,subprocess
from time import sleep
class PythonSchoolCommand(sublime_plugin.WindowCommand):
	def run(self):
		path='/Users/vigneshm/Desktop/st_plugin/1.py'
		self.open(path)
		view_curr=self.window.active_view()
		print (view_curr.file_name())
		view_curr.run_command('save')
		print (view_curr.file_name())
		view_curr.run_command('insert_text',{'pos':0,'text':'Hello\n'})
		#insert_edit=view_curr.begin_edit()
		#view_curr.insert(insert_edit,0,"# Try typing print('Hello World')\n")
		#view_curr.end_edit(insert_edit)

	def open(self, file):
		sublime.status_message("Trying to open " + file)
		if file == "":
			sublime.status_message("Not a valid file")
			return
		if os.path.exists(file):
			sublime.status_message("File exists " + file)
			self.window.open_file(file)
			sublime.status_message("Opening " + file)
		else:
			sublime.status_message("Cannot find file! " +  file)
			if sublime.ok_cancel_dialog("Create file? " + file):
				self.create(file)
				if(os.path.exists(file)):
					self.window.open_file(file)
				else :
					self.window.open_file(file)
					self.window.run_command('prompt_save_as')
					print ("doesnt exist")
					self.window.open_file(file)

	def create(self, filename):
		base, filename = os.path.split(filename)
		self.create_folder(base)

	def create_folder(self, base):
		if not os.path.exists(base):
			parent = os.path.split(base)[0]
			if not os.path.exists(parent):
				self.create_folder(parent)
			os.mkdir(base)

class CheckOutputCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		fname=self.view.file_name();
		proc = subprocess.Popen(['python', fname], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		output= proc.communicate()[0]
		print (output)

class InsertTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, pos, text):
        self.view.insert(edit, pos, text)
        print ("printing "+text)
