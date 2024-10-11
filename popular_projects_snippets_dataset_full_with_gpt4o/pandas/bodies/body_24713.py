# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
width = self._width_to_float(width_input)
if width < 1e-5:
    exit(None)
elif width < 1.3:
    exit("thin")
elif width < 2.8:
    exit("medium")
exit("thick")
