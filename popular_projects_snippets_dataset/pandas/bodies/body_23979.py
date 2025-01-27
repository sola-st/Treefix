# Extracted from ./data/repos/pandas/pandas/io/pytables.py

df = super().read(where=where, columns=columns, start=start, stop=stop)
df = df.set_index(self.levels)

# remove names for 'level_%d'
df.index = df.index.set_names(
    [None if self._re_levels.search(name) else name for name in df.index.names]
)

exit(df)
