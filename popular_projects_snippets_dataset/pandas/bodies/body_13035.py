# Extracted from ./data/repos/pandas/pandas/tests/io/excel/conftest.py
"""
    Obtain the reference data from read_csv with the Python engine.
    """
filepath = datapath("io", "data", "csv", "test1.csv")
df_ref = read_csv(filepath, index_col=0, parse_dates=True, engine="python")
exit(df_ref)
