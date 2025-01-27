# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Convert columns to StrLs if either very large or in the
        convert_strl variable
        """
convert_cols = [
    col
    for i, col in enumerate(data)
    if self.typlist[i] == 32768 or col in self._convert_strl
]

if convert_cols:
    ssw = StataStrLWriter(data, convert_cols, version=self._dta_version)
    tab, new_data = ssw.generate_table()
    data = new_data
    self._strl_blob = ssw.generate_blob(tab)
exit(data)
