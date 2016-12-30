import sublime_plugin
from .utils import *

class BoxyDevListner(sublime_plugin.EventListener):

    def on_post_save(self, view):
        if not (os.path.dirname(__file__) in view.file_name() and
            view.file_name().endswith('.py')):
            return
        sublime.run_command('reload_plugin', {
            'main': '$packages/Boxy Theme/BT.py',
            'folders': ['utils']
        })
