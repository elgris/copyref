import sublime, sublime_plugin
import os
import string

# CopyrefCommand takes reference to current line in the file and copies it to clipboard
# in behves similar to "Copy Reference" in Intellij IDEA. That is, it uses path to file
# relative to project root instead of full path. If project root could not be 
# determined - it will use full path
class CopyrefCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        """

        """
        ref = self.view.file_name()
        if ref is None:
            return
        
        baseDir = os.path.abspath(self.base_dir())
        if baseDir[len(baseDir)-1] != os.sep:
            baseDir += os.sep # normalize baseDir, it has to end with separator

        if ref.find(baseDir) == 0:
            ref = ref[len(baseDir):]

        (row, col) = self.view.rowcol(self.view.sel()[0].begin())
        row+=1 # row is zero-based, normalizing it

        pos = "{:s}:{:d}".format(ref, row)

        sublime.set_clipboard(pos)


    def base_dir(self):
        """
        base_dir returns base directory of current project.
        It can take "base_dir" configuration option from *.sublime-project file
        Otherwise it will try to get 1st folder listed in *.sublime-project
        """
        projectData = self.view.window().project_data()
        if "base_dir" in projectData:
            return projectData["base_dir"]

        if "folders" in projectData and projectData["folders"]:
            baseFolder = projectData["folders"][0]
            if "path" in baseFolder:
                return baseFolder["path"]

        projectFileName = self.view.window().project_file_name()
        if projectFileName:
            return os.path.dirname(projectFileName)