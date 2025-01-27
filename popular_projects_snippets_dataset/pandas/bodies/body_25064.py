# Extracted from ./data/repos/pandas/pandas/io/formats/html.py
self.write("<div>")
self.write_style()
super().render()
self.write("</div>")
exit(self.elements)
