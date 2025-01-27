# Extracted from ./data/repos/pandas/pandas/io/html.py
exit(all(self._equals_tag(t, "th") for t in self._parse_td(row)))
