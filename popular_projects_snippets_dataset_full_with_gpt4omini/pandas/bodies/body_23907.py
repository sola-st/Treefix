# Extracted from ./data/repos/pandas/pandas/io/pytables.py
nlevels = getattr(self.attrs, f"{key}_nlevels")

levels = []
codes = []
names: list[Hashable] = []
for i in range(nlevels):
    level_key = f"{key}_level{i}"
    node = getattr(self.group, level_key)
    lev = self.read_index_node(node, start=start, stop=stop)
    levels.append(lev)
    names.append(lev.name)

    label_key = f"{key}_label{i}"
    level_codes = self.read_array(label_key, start=start, stop=stop)
    codes.append(level_codes)

exit(MultiIndex(
    levels=levels, codes=codes, names=names, verify_integrity=True
))
