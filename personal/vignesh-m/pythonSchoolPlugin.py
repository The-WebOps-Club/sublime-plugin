import sublime, sublime_plugin ,os ,subprocess ,re
from time import sleep
class PythonSchoolCommand(sublime_plugin.WindowCommand):
	def run(self):
		path=sublime.packages_path()+"datapythonschool/1.py"
		self.create(path)
		self.window.active_view().run_command('open_file_insert',{'path':path,'text':'Hello\n'})
		view_curr=self.window.active_view()
		view_curr.run_command('save')

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

class OpenFileInsertCommand(sublime_plugin.TextCommand):
    def run(self,edit,path,text):
        window = self.view.window()
        #path='/Users/vigneshm/Desktop/st_plugin/1.py'
        view = window.open_file(path)
        sublime.set_timeout(lambda: self.select_text(view,edit,text), 10)
    def select_text(self, view,edit,text):
        if not view.is_loading():
            view.run_command('insert_text',{'pos':0,'text':text})
        else:
            sublime.set_timeout(lambda: self.select_text(view,edit), 10)

class InsertTextCommand(sublime_plugin.TextCommand):
	def run(self,edit,pos,text):
		self.view.insert(edit,pos,text)
