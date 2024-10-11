# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Generates the GSO lookup table for the DataFrame

        Returns
        -------
        gso_table : dict
            Ordered dictionary using the string found as keys
            and their lookup position (v,o) as values
        gso_df : DataFrame
            DataFrame where strl columns have been converted to
            (v,o) values

        Notes
        -----
        Modifies the DataFrame in-place.

        The DataFrame returned encodes the (v,o) values as uint64s. The
        encoding depends on the dta version, and can be expressed as

        enc = v + o * 2 ** (o_size * 8)

        so that v is stored in the lower bits and o is in the upper
        bits. o_size is

          * 117: 4
          * 118: 6
          * 119: 5
        """
gso_table = self._gso_table
gso_df = self.df
columns = list(gso_df.columns)
selected = gso_df[self.columns]
col_index = [(col, columns.index(col)) for col in self.columns]
keys = np.empty(selected.shape, dtype=np.uint64)
for o, (idx, row) in enumerate(selected.iterrows()):
    for j, (col, v) in enumerate(col_index):
        val = row[col]
        # Allow columns with mixed str and None (GH 23633)
        val = "" if val is None else val
        key = gso_table.get(val, None)
        if key is None:
            # Stata prefers human numbers
            key = (v + 1, o + 1)
            gso_table[val] = key
        keys[o, j] = self._convert_key(key)
for i, col in enumerate(self.columns):
    gso_df[col] = keys[:, i]

exit((gso_table, gso_df))
