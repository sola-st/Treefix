# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 39465
df = DataFrame({"ABC": [1]})
path = tmp_path / filename
df.to_csv(path, compression="zip")
with ZipFile(path) as zp:
    assert len(zp.filelist) == 1
    archived_file = zp.filelist[0].filename
    assert archived_file == expected_arcname
