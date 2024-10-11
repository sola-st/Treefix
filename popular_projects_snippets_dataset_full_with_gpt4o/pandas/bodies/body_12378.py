# Extracted from ./data/repos/pandas/pandas/tests/io/test_s3.py
# GH 34626
# Use Amazon Open Data Registry - https://registry.opendata.aws/gdelt
result = read_csv("s3://gdelt-open-data/events/1981.csv", nrows=3)
assert len(result) == 3
