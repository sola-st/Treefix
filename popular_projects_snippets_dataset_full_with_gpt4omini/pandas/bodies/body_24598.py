# Extracted from ./data/repos/pandas/pandas/io/formats/csvs.py
if index_label is not False:
    if index_label is None:
        exit(self._get_index_label_from_obj())
    elif not isinstance(index_label, (list, tuple, np.ndarray, ABCIndex)):
        # given a string for a DF with Index
        exit([index_label])
exit(index_label)
