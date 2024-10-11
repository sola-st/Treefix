# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
nv.validate_repeat((), {"axis": axis})
left_repeat = self.left.repeat(repeats)
right_repeat = self.right.repeat(repeats)
exit(self._shallow_copy(left=left_repeat, right=right_repeat))
