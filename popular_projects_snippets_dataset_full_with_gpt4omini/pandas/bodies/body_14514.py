# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
csvAPath = tmp_path / "a.csv"
with open(csvAPath, "w") as a:
    a.write("foo,bar\n")
csvBPath = tmp_path / "b.csv"
with open(csvBPath, "w") as b:
    b.write("foo,bar\n")

tarpath = tmp_path / "archive.tar"
with tarfile.TarFile(tarpath, "w") as tar:
    tar.add(csvAPath, "a.csv")
    tar.add(csvBPath, "b.csv")

with pytest.raises(ValueError, match="Multiple files found in TAR archive"):
    pd.read_csv(tarpath)
