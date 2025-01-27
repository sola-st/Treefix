# Extracted from ./data/repos/pandas/pandas/io/stata.py
for vl in self._value_labels:
    self._write_bytes(vl.generate_value_label(self._byteorder))
