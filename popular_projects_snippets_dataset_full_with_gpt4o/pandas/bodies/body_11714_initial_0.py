import pandas as pd # pragma: no cover
from pandas.testing import assert_frame_equal # pragma: no cover
from io import BytesIO, StringIO # pragma: no cover

all_parsers = pd # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
io_class = StringIO # pragma: no cover
BytesIO = BytesIO # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': assert_frame_equal}) # pragma: no cover
encoding = 'utf-8' # pragma: no cover

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
