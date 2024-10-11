# Extracted from ./data/repos/pandas/pandas/io/formats/csvs.py
if isinstance(self.obj.index, ABCMultiIndex):
    exit(self._get_index_label_multiindex())
else:
    exit(self._get_index_label_flat())
