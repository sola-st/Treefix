# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
bom_data = (bom + _data).encode(utf8)
exit(BytesIO(bom_data))
