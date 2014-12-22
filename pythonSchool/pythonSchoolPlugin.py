import sublime, sublime_plugin ,os ,subprocess ,re ,sys ,StringIO
from time import sleep
class PythonSchoolCommand(sublime_plugin.WindowCommand):
	def run(self):
		path=sublime.packages_path()+"/PythonSchool/datapythonschool/1.py"
		self.create(path)
		view_curr=self.window.open_file(path)
		view_curr.run_command('erase_all');
		view_curr.run_command('insert_text',{'pos':0,'text':"# Write a program to print Hello to stdout\n"})
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
			try :
				os.mkdir(base)
			except :
				print ('Error while opening file');

class CheckOutputCommand(sublime_plugin.TextCommand):
	

	def getnum(self,filepath):
		name=os.path.basename(filepath)
		n=int(name.split('.py')[0])
		return n

	def run(self,edit):
		fname=self.view.file_name();
		n=self.getnum(fname)
		proc = subprocess.Popen(['python', fname], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		output= proc.communicate()[0]
		solnfname=os.path.dirname(fname)+"/"+str(n)+"soln.py"
		proc2 = subprocess.Popen(['python',solnfname ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		output2= proc2.communicate()[0]
		solnfile=open(solnfname,'r')
		view=self.view
		view.run_command('move_to',{'to':'eof'})
		view.insert(edit,view.sel()[0].begin(),"\n#----\tYour Output:\t---#\n\n"+(output.decode('utf-8'))+"\n\n#----\tYour Output End\t---#\n");
		view.insert(edit,view.sel()[0].begin(),"\n#----\tExpected Output:\t---#\n\n"+(output2.decode('utf-8'))+"\n\n#----\tExpected Output End\t---#\n");
		view.insert(edit,view.sel()[0].begin(),"\n#----\tModel Solution:\t---#\n\n"+solnfile.read()+"\n\n#----\tModel Solution End\t---#\n");
		print (output)

class InsertTextCommand(sublime_plugin.TextCommand):
	def run(self,edit,pos,text):
		self.view.insert(edit,pos,text)

class EraseAllCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		self.view.erase(edit,sublime.Region(0,self.view.size()))
