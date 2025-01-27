# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""Encode value labels."""

self.text_len = 0
self.txt: list[bytes] = []
self.n = 0
# Offsets (length of categories), converted to int32
self.off = np.array([], dtype=np.int32)
# Values, converted to int32
self.val = np.array([], dtype=np.int32)
self.len = 0

# Compute lengths and setup lists of offsets and labels
offsets: list[int] = []
values: list[float] = []
for vl in self.value_labels:
    category: str | bytes = vl[1]
    if not isinstance(category, str):
        category = str(category)
        warnings.warn(
            value_label_mismatch_doc.format(self.labname),
            ValueLabelTypeMismatch,
            stacklevel=find_stack_level(),
        )
    category = category.encode(self._encoding)
    offsets.append(self.text_len)
    self.text_len += len(category) + 1  # +1 for the padding
    values.append(vl[0])
    self.txt.append(category)
    self.n += 1

if self.text_len > 32000:
    raise ValueError(
        "Stata value labels for a single variable must "
        "have a combined length less than 32,000 characters."
    )

# Ensure int32
self.off = np.array(offsets, dtype=np.int32)
self.val = np.array(values, dtype=np.int32)

# Total length
self.len = 4 + 4 + 4 * self.n + 4 * self.n + self.text_len
