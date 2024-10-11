# Extracted from ./data/repos/scrapy/scrapy/exporters.py
self._beautify_indent(depth=depth)
self.xg.startElement(name, {})
if hasattr(serialized_value, 'items'):
    self._beautify_newline()
    for subname, value in serialized_value.items():
        self._export_xml_field(subname, value, depth=depth + 1)
    self._beautify_indent(depth=depth)
elif is_listlike(serialized_value):
    self._beautify_newline()
    for value in serialized_value:
        self._export_xml_field('value', value, depth=depth + 1)
    self._beautify_indent(depth=depth)
elif isinstance(serialized_value, str):
    self.xg.characters(serialized_value)
else:
    self.xg.characters(str(serialized_value))
self.xg.endElement(name)
self._beautify_newline()
