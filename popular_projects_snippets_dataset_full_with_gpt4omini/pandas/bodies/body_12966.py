# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# GH#36712
if read_ext in (".xlsb", ".xls"):
    pytest.skip(f"No engine for filetype: '{read_ext}'")

import pyarrow as pa

with pd.option_context("mode.string_storage", string_storage):

    df = DataFrame(
        {
            "a": np.array(["a", "b"], dtype=np.object_),
            "b": np.array(["x", pd.NA], dtype=np.object_),
        }
    )
    with tm.ensure_clean(read_ext) as file_path:
        df.to_excel(file_path, "test", index=False)
        result = pd.read_excel(
            file_path, sheet_name="test", use_nullable_dtypes=True
        )

    if string_storage == "python":
        expected = DataFrame(
            {
                "a": StringArray(np.array(["a", "b"], dtype=np.object_)),
                "b": StringArray(np.array(["x", pd.NA], dtype=np.object_)),
            }
        )
    else:
        expected = DataFrame(
            {
                "a": ArrowStringArray(pa.array(["a", "b"])),
                "b": ArrowStringArray(pa.array(["x", None])),
            }
        )
    tm.assert_frame_equal(result, expected)
