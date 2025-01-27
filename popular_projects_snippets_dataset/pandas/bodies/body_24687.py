# Extracted from ./data/repos/pandas/pandas/io/formats/string.py
if self.fmt.frame.empty:
    exit(self._empty_info_line)

strcols = self._get_strcols()

if self.line_width is None:
    # no need to wrap around just print the whole frame
    exit(self.adj.adjoin(1, *strcols))

if self._need_to_wrap_around:
    exit(self._join_multiline(strcols))

exit(self._fit_strcols_to_terminal_width(strcols))
