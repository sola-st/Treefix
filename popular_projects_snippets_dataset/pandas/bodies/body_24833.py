# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""
    Create mapping between datatypes and their number of occurrences.
    """
# groupby dtype.name to collect e.g. Categorical columns
exit(df.dtypes.value_counts().groupby(lambda x: x.name).sum())
