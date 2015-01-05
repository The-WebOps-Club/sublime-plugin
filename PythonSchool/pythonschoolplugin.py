import sublime, sublime_plugin ,os ,subprocess ,re ,sys ,io
from time import sleep
class PythonSchoolCommand(sublime_plugin.TextCommand):
	def run(self,edit,num):
		#print(num)
		path=sublime.packages_path()+"/PythonSchool/datapythonschool/"+num+".py"
		prob=sublime.packages_path()+"/PythonSchool/datapythonschool/"+num+"prob";
		probfile=open(prob);
		self.create(path)
		view_curr=self.view.window().open_file(path)
		if(view_curr.is_loading()):
			sublime.set_timeout(lambda:self.run(edit,num),10)
		view_curr.run_command('erase_all');
		view_curr.run_command('insert_text',{'pos':0,'text':probfile.read()})
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
		inputfname=os.path.dirname(fname)+"/"+str(n)+"input"
		inputfile=open(inputfname,'r')
		inputtext=inputfile.read()
		inputbytes=inputtext.encode("utf8","replace")
		print(inputbytes)
		proc = subprocess.Popen(['python', fname], stdout=subprocess.PIPE,stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
		output= proc.communicate(input=inputbytes)[0]
		if(proc.returncode==None):
			proc.terminate()
		solnfname=os.path.dirname(fname)+"/"+str(n)+"soln.py"
		proc2 = subprocess.Popen(['python',solnfname ], stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.STDOUT)
		output2= proc2.communicate(input=inputbytes)[0]
		
		if(proc2.returncode==None):
			proc2.terminate()
		solnfile=open(solnfname,'r')
		view=self.view
		view.run_command('move_to',{'to':'eof'})
		status=-1
		if(output.decode("utf-8")==output2.decode("utf-8")):
			status=1
		else :
			status=0
		if(status==1) :
			view.insert(edit,view.sel()[0].begin(),"\n\n#\tCorrect!\n");
		else :
			view.insert(edit,view.sel()[0].begin(),"\n\n#\tTry Again\n");
		if(inputtext!=""):
			view.insert(edit,view.sel()[0].begin(),"\n#----\tInput:\t---#\n\n"+inputtext+"\n\n#----\tInput End\t---#\n");
		view.insert(edit,view.sel()[0].begin(),"\n#----\tYour Output:\t---#\n\n"+(output.decode('utf-8'))+"\n\n#----\tYour Output End\t---#\n");
		view.insert(edit,view.sel()[0].begin(),"\n#----\tExpected Output:\t---#\n\n"+(output2.decode('utf-8'))+"\n\n#----\tExpected Output End\t---#\n");
		if(status == 1) :
			view.insert(edit,view.sel()[0].begin(),"\n#----\tModel Solution:\t---#\n\n"+solnfile.read()+"\n\n#----\tModel Solution End\t---#\n");

class InsertTextCommand(sublime_plugin.TextCommand):
	def run(self,edit,pos,text):
		self.view.insert(edit,pos,text)

class EraseAllCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		self.view.erase(edit,sublime.Region(0,self.view.size()))
