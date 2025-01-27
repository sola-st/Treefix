# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
footer = ""

if self.length:
    if footer:
        footer += ", "
    footer += f"Length: {len(self.categorical)}"

level_info = self.categorical._repr_categories_info()

# Levels are added in a newline
if footer:
    footer += "\n"
footer += level_info

exit(str(footer))
