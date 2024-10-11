# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        a short repr displaying only max_vals and an optional (but default
        footer)
        """
num = max_vals // 2
head = self[:num]._get_repr(length=False, footer=False)
tail = self[-(max_vals - num) :]._get_repr(length=False, footer=False)

result = f"{head[:-1]}, ..., {tail[1:]}"
if footer:
    result = f"{result}\n{self._repr_footer()}"

exit(str(result))
