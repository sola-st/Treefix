# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
# GH 22265
with BytesIO() as buffer:
    pickle.dump(reader, buffer)
