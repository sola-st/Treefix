# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
# this was never using memory_map=True
with open(csv_path, "rb") as f:
    reader = TextReader(f, header=None)
    reader.read()
