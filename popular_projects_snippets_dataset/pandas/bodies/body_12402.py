# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
from pyarrow import csv

# Test latin1, ucs-2, and ucs-4 chars
data = """a,b,c
1,2,3
©,®,®
Look,a snake,🐍"""
expected = pd.DataFrame(
    {"a": ["1", "©", "Look"], "b": ["2", "®", "a snake"], "c": ["3", "®", "🐍"]}
)
s = StringIO(data)
with icom.get_handle(s, "rb", is_text=False) as handles:
    df = csv.read_csv(handles.handle).to_pandas()
    tm.assert_frame_equal(df, expected)
    assert not s.closed
