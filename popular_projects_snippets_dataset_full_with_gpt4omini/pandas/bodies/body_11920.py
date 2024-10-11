# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
with open(csv_path, "rb") as f:
    text = f.read()
src = BytesIO(text)
reader = TextReader(src, header=None)
reader.read()
