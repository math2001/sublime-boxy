import sublime_plugin
from .utils import *

class BoxyDevListner(sublime_plugin.EventListener):

    def on_post_save(self, view):
        if os.path.dirname(__file__) not in view.file_name():
            return
        sublime.run_command('reload_plugin', {
            'main': '$packages/Boxy Theme/BT.py',
            'folders': ['utils']
        })
