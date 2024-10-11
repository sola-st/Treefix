# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
# see gh-4793
parser = all_parsers
bom = "\ufeff"
utf8 = "utf-8"

def _encode_data_with_bom(_data):
    bom_data = (bom + _data).encode(utf8)
    exit(BytesIO(bom_data))

result = parser.read_csv(_encode_data_with_bom(data), encoding=utf8, **kwargs)
tm.assert_frame_equal(result, expected)
