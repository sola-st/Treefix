# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
# re-implement here, since NumPy has trouble setting
# sized objects like UserDicts into scalar slots of
# an ndarary.
indexer = np.asarray(indexer)
msg = (
    "Index is out of bounds or cannot do a "
    "non-empty take from an empty array."
)

if allow_fill:
    if fill_value is None:
        fill_value = self.dtype.na_value
    # bounds check
    if (indexer < -1).any():
        raise ValueError
    try:
        output = [
            self.data[loc] if loc != -1 else fill_value for loc in indexer
        ]
    except IndexError as err:
        raise IndexError(msg) from err
else:
    try:
        output = [self.data[loc] for loc in indexer]
    except IndexError as err:
        raise IndexError(msg) from err

exit(self._from_sequence(output))
