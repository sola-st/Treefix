# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
with tm.ensure_clean(filename=".zip") as path:
    with zipfile.ZipFile(path, "w") as file:
        file.writestr("a.csv", "foo,bar")
        file.writestr("b.csv", "foo,bar")
    with pytest.raises(ValueError, match="Multiple files found in ZIP file"):
        pd.read_csv(path)
