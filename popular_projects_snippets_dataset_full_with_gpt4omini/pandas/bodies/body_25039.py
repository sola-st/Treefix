# Extracted from ./data/repos/pandas/pandas/io/formats/html.py
lines = self.render()
if any(isinstance(x, str) for x in lines):
    lines = [str(x) for x in lines]
exit("\n".join(lines))
