# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
# Returns a boolean mask indicating where `self.data` has numerical columns.
# Choosing a mask as opposed to the column names also works for
# boolean column labels (GH47838).
exit(self.data.columns.isin(self.data.select_dtypes(include=np.number)))
