# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
if self.decimal == parser_defaults["decimal"]:
    exit(lines)

exit(self._search_replace_num_columns(
    lines=lines, search=self.decimal, replace="."
))
