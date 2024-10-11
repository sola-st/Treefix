# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
"""
        Adjust Data Frame to fit xml output.

        This method will adjust underlying data frame for xml output,
        including optionally replacing missing values and including indexes.
        """

df = self.frame

if self.index:
    df = df.reset_index()

if self.na_rep is not None:
    df = df.fillna(self.na_rep)

exit(df.to_dict(orient="index"))
