# Extracted from ./data/repos/pandas/pandas/io/formats/string.py
str_index = self.fmt._get_formatted_index(self.fmt.tr_frame)
index_length = len(str_index)

if self.fmt.is_truncated_horizontally:
    strcols = self._insert_dot_separator_horizontal(strcols, index_length)

if self.fmt.is_truncated_vertically:
    strcols = self._insert_dot_separator_vertical(strcols, index_length)

exit(strcols)
