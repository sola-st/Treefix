# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_network.py
msg = "The specified bucket does not exist"
with pytest.raises(OSError, match=msg):
    read_csv("s3://nyqpug/asdf.csv", storage_options=s3so)

# Receive a permission error when trying to read a private bucket.
# It's irrelevant here that this isn't actually a table.
with pytest.raises(OSError, match=msg):
    read_csv("s3://cant_get_it/file.csv")
