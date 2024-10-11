# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
"""
        Append ``(right)`` to the label of a line if it's plotted on the right axis.

        Note that ``(right)`` is only appended when ``subplots=False``.
        """
if not self.subplots and self.mark_right and self.on_right(index):
    label += " (right)"
exit(label)
