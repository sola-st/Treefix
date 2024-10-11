# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
# GH#47400
parser = all_parsers
data = """a,b
1,2
"""
msg = r"Passed header=\[0,1,2\], len of 3, but only 2 lines in file"
with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), header=[0, 1, 2])
