import sublime, sublime_plugin


class OldLinesListener(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		settings = sublime.load_settings('Preferences.sublime-settings')

		if settings.get('kill_ending_blank_lines_on_save'):
			view.run_command('kill_ending_blank_lines')


class LinesKiller(sublime_plugin.TextCommand):
	def last_newline(self):
		view = self.view
		size = view.size()

		return sublime.Region(size - 1, size)

	def kill(self, edit, line, incliding_last_line=True):
		view = self.view
		size = view.size()

		last = line.end() == size
		line = sublime.Region(line.a, line.b + 1)

		view.erase(edit, line)

		if incliding_last_line and last:
			view.erase(edit, self.last_newline())

	def kill_blank_lines(self, edit, direction='above', pos=None):
		view = self.view
		size = view.size()
		above = direction == 'above'

		if above:
			begin = 0
			end = pos or size
		else:
			begin = pos or 0
			end = size

		if end == 0:
			return

		lines = view.lines(sublime.Region(begin, end))

		if end == size:
			lines.append(self.last_newline())

		if above:
			lines.reverse()

		scope = []

		for line in lines:
			if line.empty() or view.substr(line).strip() == '':
				scope.append(line)
			else:
				if above and pos > line.b:
					scope.append(sublime.Region(line.b, line.b))

				break

		if not above:
			scope.reverse()

		for line in scope:
			self.kill(edit, line, not above)


class KillLineCommand(LinesKiller):
	def run(self, edit):
		view = self.view

		selections = list(view.sel())
		selections.reverse()

		for sel in selections:
			self.kill(edit, view.line(sel))


class KillEndingBlankLinesCommand(LinesKiller):
	def run(self, edit):
		self.kill_blank_lines(edit, 'above')


class KillBlankLinesAboveCommand(LinesKiller):
	def run(self, edit):
		for sel in self.view.sel():
			self.kill_blank_lines(edit, 'above', sel.end())


class KillBlankLinesBelowCommand(LinesKiller):
	def run(self, edit):
		for sel in self.view.sel():
			self.kill_blank_lines(edit, 'below', sel.begin())