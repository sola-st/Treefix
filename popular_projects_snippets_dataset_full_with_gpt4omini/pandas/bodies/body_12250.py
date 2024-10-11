# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
pytest.importorskip("openpyxl")
extension = "xlsx"

df = DataFrame({"a": [0]})

path = f"testmem://test/test.{extension}"

df.to_excel(path, storage_options={"test": "write"}, index=False)
assert fsspectest.test[0] == "write"
read_excel(path, storage_options={"test": "read"})
assert fsspectest.test[0] == "read"
