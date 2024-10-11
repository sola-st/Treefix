# Extracted from ./data/repos/pandas/pandas/io/html.py
"""
        Given a list of <tr>s, return a list of text rows.

        Parameters
        ----------
        rows : list of node-like
            List of <tr>s
        section : the section that the rows belong to (header, body or footer).

        Returns
        -------
        list of list
            Each returned row is a list of str text, or tuple (text, link)
            if extract_links is not None.

        Notes
        -----
        Any cell with ``rowspan`` or ``colspan`` will have its contents copied
        to subsequent cells.
        """
all_texts = []  # list of rows, each a list of str
text: str | tuple
remainder: list[
    tuple[int, str | tuple, int]
] = []  # list of (index, text, nrows)

for tr in rows:
    texts = []  # the output for this row
    next_remainder = []

    index = 0
    tds = self._parse_td(tr)
    for td in tds:
        # Append texts from previous rows with rowspan>1 that come
        # before this <td>
        while remainder and remainder[0][0] <= index:
            prev_i, prev_text, prev_rowspan = remainder.pop(0)
            texts.append(prev_text)
            if prev_rowspan > 1:
                next_remainder.append((prev_i, prev_text, prev_rowspan - 1))
            index += 1

        # Append the text from this <td>, colspan times
        text = _remove_whitespace(self._text_getter(td))
        if self.extract_links in ("all", section):
            href = self._href_getter(td)
            text = (text, href)
        rowspan = int(self._attr_getter(td, "rowspan") or 1)
        colspan = int(self._attr_getter(td, "colspan") or 1)

        for _ in range(colspan):
            texts.append(text)
            if rowspan > 1:
                next_remainder.append((index, text, rowspan - 1))
            index += 1

            # Append texts from previous rows at the final position
    for prev_i, prev_text, prev_rowspan in remainder:
        texts.append(prev_text)
        if prev_rowspan > 1:
            next_remainder.append((prev_i, prev_text, prev_rowspan - 1))

    all_texts.append(texts)
    remainder = next_remainder

# Append rows that only appear because the previous row had non-1
# rowspan
while remainder:
    next_remainder = []
    texts = []
    for prev_i, prev_text, prev_rowspan in remainder:
        texts.append(prev_text)
        if prev_rowspan > 1:
            next_remainder.append((prev_i, prev_text, prev_rowspan - 1))
    all_texts.append(texts)
    remainder = next_remainder

exit(all_texts)
