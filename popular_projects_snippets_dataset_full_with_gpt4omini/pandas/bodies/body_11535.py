# Extracted from ./data/repos/pandas/pandas/tests/io/xml/test_xml.py
# GH#50500
if string_storage == "pyarrow" or dtype_backend == "pyarrow":
    pa = pytest.importorskip("pyarrow")
data = """<?xml version='1.0' encoding='utf-8'?>
<data xmlns="http://example.com">
<row>
  <a>x</a>
  <b>1</b>
  <c>4.0</c>
  <d>x</d>
  <e>2</e>
  <f>4.0</f>
  <g></g>
  <h>True</h>
  <i>False</i>
</row>
<row>
  <a>y</a>
  <b>2</b>
  <c>5.0</c>
  <d></d>
  <e></e>
  <f></f>
  <g></g>
  <h>False</h>
  <i></i>
</row>
</data>"""

if string_storage == "python":
    string_array = StringArray(np.array(["x", "y"], dtype=np.object_))
    string_array_na = StringArray(np.array(["x", NA], dtype=np.object_))

else:
    string_array = ArrowStringArray(pa.array(["x", "y"]))
    string_array_na = ArrowStringArray(pa.array(["x", None]))

with pd.option_context("mode.string_storage", string_storage):
    with pd.option_context("mode.dtype_backend", dtype_backend):
        result = read_xml(data, parser=parser, use_nullable_dtypes=True)

expected = DataFrame(
    {
        "a": string_array,
        "b": Series([1, 2], dtype="Int64"),
        "c": Series([4.0, 5.0], dtype="Float64"),
        "d": string_array_na,
        "e": Series([2, NA], dtype="Int64"),
        "f": Series([4.0, NA], dtype="Float64"),
        "g": Series([NA, NA], dtype="Int64"),
        "h": Series([True, False], dtype="boolean"),
        "i": Series([False, NA], dtype="boolean"),
    }
)

if dtype_backend == "pyarrow":
    from pandas.arrays import ArrowExtensionArray

    expected = DataFrame(
        {
            col: ArrowExtensionArray(pa.array(expected[col], from_pandas=True))
            for col in expected.columns
        }
    )
    expected["g"] = ArrowExtensionArray(pa.array([None, None]))

tm.assert_frame_equal(result, expected)
