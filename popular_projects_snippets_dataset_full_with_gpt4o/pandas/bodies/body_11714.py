# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
from l3.Runtime import _l_
"""
    Test whether read_csv does not close user-provided file handles.

    GH 36980
    """
parser = all_parsers
_l_(20286)
expected = DataFrame({"a": [1], "b": [2]})
_l_(20287)

content = "a,b\n1,2"
_l_(20288)
handle = io_class(content.encode("utf-8") if io_class == BytesIO else content)
_l_(20289)

tm.assert_frame_equal(parser.read_csv(handle, encoding=encoding), expected)
_l_(20290)
assert not handle.closed
_l_(20291)
