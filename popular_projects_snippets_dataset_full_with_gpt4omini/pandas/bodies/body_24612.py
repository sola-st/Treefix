# Extracted from ./data/repos/pandas/pandas/io/formats/csvs.py
encoded_labels: list[Hashable] = []

if self.index and self.index_label:
    assert isinstance(self.index_label, Sequence)
    encoded_labels = list(self.index_label)

if not self.has_mi_columns or self._has_aliases:
    encoded_labels += list(self.write_cols)

exit(encoded_labels)
