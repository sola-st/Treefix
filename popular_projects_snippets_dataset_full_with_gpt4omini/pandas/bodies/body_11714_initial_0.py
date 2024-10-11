import pandas as pd # pragma: no cover
import io # pragma: no cover
import pandas.testing as tm # pragma: no cover

all_parsers = [pd] # pragma: no cover
DataFrame = pd.DataFrame # pragma: no cover
io_class = io.StringIO # pragma: no cover
BytesIO = io.BytesIO # pragma: no cover
encoding = 'utf-8' # pragma: no cover
tm.assert_frame_equal = type('Mock', (object,), {'assert_frame_equal': tm.assert_frame_equal}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
from l3.Runtime import _l_
"""
    Test whether read_csv does not close user-provided file handles.

    GH 36980
    """
parser = all_parsers
_l_(8716)
expected = DataFrame({"a": [1], "b": [2]})
_l_(8717)

content = "a,b\n1,2"
_l_(8718)
handle = io_class(content.encode("utf-8") if io_class == BytesIO else content)
_l_(8719)

tm.assert_frame_equal(parser.read_csv(handle, encoding=encoding), expected)
_l_(8720)
assert not handle.closed
_l_(8721)
