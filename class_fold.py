import sublime
import sublime_plugin

class ClassFoldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        classPoints = self.view.find_all(' class=\"([^"]*)\"');
        for point in classPoints:
            point.a = point.a + 6;

        if self.view.fold(classPoints) == False:
            self.view.unfold(classPoints);
