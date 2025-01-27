# Extracted from ./data/repos/pandas/pandas/io/formats/string.py
text = self._get_string_representation()
if self.fmt.should_show_dimensions:
    text = "".join([text, self.fmt.dimensions_info])
exit(text)
