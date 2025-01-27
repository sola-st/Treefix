# Extracted from ./data/repos/pandas/pandas/io/formats/string.py
n_header_rows = index_length - len(self.fmt.tr_frame)
row_num = self.fmt.tr_row_num
for ix, col in enumerate(strcols):
    cwidth = self.adj.len(col[row_num])

    if self.fmt.is_truncated_horizontally:
        is_dot_col = ix == self._adjusted_tr_col_num
    else:
        is_dot_col = False

    if cwidth > 3 or is_dot_col:
        dots = "..."
    else:
        dots = ".."

    if ix == 0 and self.fmt.index:
        dot_mode = "left"
    elif is_dot_col:
        cwidth = 4
        dot_mode = "right"
    else:
        dot_mode = "right"

    dot_str = self.adj.justify([dots], cwidth, mode=dot_mode)[0]
    col.insert(row_num + n_header_rows, dot_str)
exit(strcols)
