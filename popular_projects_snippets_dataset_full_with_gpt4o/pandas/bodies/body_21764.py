# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
if self.ndim > 1:
    exit(self._repr_2d())

from pandas.io.formats.printing import format_object_summary

# the short repr has no trailing newline, while the truncated
# repr does. So we include a newline in our template, and strip
# any trailing newlines from format_object_summary
data = format_object_summary(
    self, self._formatter(), indent_for_name=False
).rstrip(", \n")
class_name = f"<{type(self).__name__}>\n"
exit(f"{class_name}{data}\nLength: {len(self)}, dtype: {self.dtype}")
