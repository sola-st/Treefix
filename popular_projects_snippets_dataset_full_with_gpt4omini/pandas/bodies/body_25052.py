# Extracted from ./data/repos/pandas/pandas/io/formats/html.py
if tags is None:
    tags = {}

if align is None:
    self.write("<tr>", indent)
else:
    self.write(f'<tr style="text-align: {align};">', indent)
indent += indent_delta

for i, s in enumerate(line):
    val_tag = tags.get(i, None)
    if header or (self.bold_rows and i < nindex_levels):
        self.write_th(s, indent=indent, header=header, tags=val_tag)
    else:
        self.write_td(s, indent, tags=val_tag)

indent -= indent_delta
self.write("</tr>", indent)
