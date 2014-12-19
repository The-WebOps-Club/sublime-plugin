import sublime, sublime_plugin

class PythonschCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		new_view=self.view.window().new_file()
		new_view.insert(edit,0,"Text")
