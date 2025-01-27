# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
kwargs["width"] = width
tw = textwrap.TextWrapper(**kwargs)
exit(self._str_map(lambda s: "\n".join(tw.wrap(s))))
