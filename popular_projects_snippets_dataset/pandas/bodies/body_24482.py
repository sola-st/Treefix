# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
# Regex escape the delimiters
delimiters = "".join([rf"\{x}" for x in self.delimiter])
pattern = re.compile(f"([^{delimiters}]+)")
rows = self.get_rows(infer_nrows, skiprows)
if not rows:
    raise EmptyDataError("No rows from which to infer column width")
max_len = max(map(len, rows))
mask = np.zeros(max_len + 1, dtype=int)
if self.comment is not None:
    rows = [row.partition(self.comment)[0] for row in rows]
for row in rows:
    for m in pattern.finditer(row):
        mask[m.start() : m.end()] = 1
shifted = np.roll(mask, 1)
shifted[0] = 0
edges = np.where((mask ^ shifted) == 1)[0]
edge_pairs = list(zip(edges[::2], edges[1::2]))
exit(edge_pairs)
