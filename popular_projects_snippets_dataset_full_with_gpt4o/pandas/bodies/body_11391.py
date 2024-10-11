# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
# our current version pickle data
from pandas.tests.io.generate_legacy_storage_files import create_pickle_data

with catch_warnings():
    exit(create_pickle_data())
