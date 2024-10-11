# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
with io.BytesIO() as buffer:
    with icom._BytesTarFile(fileobj=buffer, mode="w"):
        pass
