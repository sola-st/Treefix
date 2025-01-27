# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
lines = self.buf
new_rows = None

# already fetched some number
if rows is not None:
    # we already have the lines in the buffer
    if len(self.buf) >= rows:
        new_rows, self.buf = self.buf[:rows], self.buf[rows:]

    # need some lines
    else:
        rows -= len(self.buf)

if new_rows is None:
    if isinstance(self.data, list):
        if self.pos > len(self.data):
            raise StopIteration
        if rows is None:
            new_rows = self.data[self.pos :]
            new_pos = len(self.data)
        else:
            new_rows = self.data[self.pos : self.pos + rows]
            new_pos = self.pos + rows

        new_rows = self._remove_skipped_rows(new_rows)
        lines.extend(new_rows)
        self.pos = new_pos

    else:
        new_rows = []
        try:
            if rows is not None:

                rows_to_skip = 0
                if self.skiprows is not None and self.pos is not None:
                    # Only read additional rows if pos is in skiprows
                    rows_to_skip = len(
                        set(self.skiprows) - set(range(self.pos))
                    )

                for _ in range(rows + rows_to_skip):
                    # assert for mypy, data is Iterator[str] or None, would
                    # error in next
                    assert self.data is not None
                    new_rows.append(next(self.data))

                len_new_rows = len(new_rows)
                new_rows = self._remove_skipped_rows(new_rows)
                lines.extend(new_rows)
            else:
                rows = 0

                while True:
                    new_row = self._next_iter_line(row_num=self.pos + rows + 1)
                    rows += 1

                    if new_row is not None:
                        new_rows.append(new_row)
                len_new_rows = len(new_rows)

        except StopIteration:
            len_new_rows = len(new_rows)
            new_rows = self._remove_skipped_rows(new_rows)
            lines.extend(new_rows)
            if len(lines) == 0:
                raise
        self.pos += len_new_rows

    self.buf = []
else:
    lines = new_rows

if self.skipfooter:
    lines = lines[: -self.skipfooter]

lines = self._check_comments(lines)
if self.skip_blank_lines:
    lines = self._remove_empty_lines(lines)
lines = self._check_thousands(lines)
exit(self._check_decimal(lines))
