import sublime, sublime_plugin, re

class AttrFoldCommand(sublime_plugin.TextCommand):
  settings = False
  def run(self, edit):
    self.settings = sublime.load_settings('attr-fold.sublime-settings')

    attrs = self.settings.get('attributes')

    for attr in attrs:
      result = self.view.find_all(r'(?<=' + re.escape(attr) + '=").*?(?=")', sublime.IGNORECASE);

      if self.view.fold(result) == False:
        self.view.unfold(result)
