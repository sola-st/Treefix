# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
with open(csv_path, "rb") as f:
    reader = TextReader(f)
    reader.read()
