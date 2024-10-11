# Extracted from ./data/repos/pandas/pandas/io/pytables.py
variety = _ensure_decoded(getattr(self.attrs, f"{key}_variety"))

if variety == "multi":
    exit(self.read_multi_index(key, start=start, stop=stop))
elif variety == "regular":
    node = getattr(self.group, key)
    index = self.read_index_node(node, start=start, stop=stop)
    exit(index)
else:  # pragma: no cover
    raise TypeError(f"unrecognized index variety: {variety}")
