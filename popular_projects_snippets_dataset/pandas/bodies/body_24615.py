# Extracted from ./data/repos/pandas/pandas/io/formats/csvs.py
if not self.has_mi_columns or self._has_aliases:
    self.writer.writerow(self.encoded_labels)
else:
    for row in self._generate_multiindex_header_rows():
        self.writer.writerow(row)
