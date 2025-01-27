# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
family = None
for name in font_names:
    family = self.FAMILY_MAP.get(name)
    if family:
        break

exit(family)
