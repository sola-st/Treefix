# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
        Render a DataFrame to a list of columns (as lists of strings).
        """
strcols = self._get_strcols_without_index()

if self.index:
    str_index = self._get_formatted_index(self.tr_frame)
    strcols.insert(0, str_index)

exit(strcols)
