# Extracted from ./data/repos/pandas/pandas/tests/io/conftest.py
"""DataFrame with the salaries dataset"""
exit(read_csv(datapath("io", "parser", "data", "salaries.csv"), sep="\t"))
