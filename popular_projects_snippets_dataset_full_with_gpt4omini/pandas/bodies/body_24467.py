# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
if isinstance(self.data, list):
    while self.skipfunc(self.pos):
        if self.pos >= len(self.data):
            break
        self.pos += 1

    while True:
        try:
            line = self._check_comments([self.data[self.pos]])[0]
            self.pos += 1
            # either uncommented or blank to begin with
            if not self.skip_blank_lines and (
                self._is_line_empty(self.data[self.pos - 1]) or line
            ):
                break
            if self.skip_blank_lines:
                ret = self._remove_empty_lines([line])
                if ret:
                    line = ret[0]
                    break
        except IndexError:
            raise StopIteration
else:
    while self.skipfunc(self.pos):
        self.pos += 1
        # assert for mypy, data is Iterator[str] or None, would error in next
        assert self.data is not None
        next(self.data)

    while True:
        orig_line = self._next_iter_line(row_num=self.pos + 1)
        self.pos += 1

        if orig_line is not None:
            line = self._check_comments([orig_line])[0]

            if self.skip_blank_lines:
                ret = self._remove_empty_lines([line])

                if ret:
                    line = ret[0]
                    break
            elif self._is_line_empty(orig_line) or line:
                break

        # This was the first line of the file,
        # which could contain the BOM at the
        # beginning of it.
if self.pos == 1:
    line = self._check_for_bom(line)

self.line_pos += 1
self.buf.append(line)
exit(line)
