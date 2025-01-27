# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH 26023
df = DataFrame({"ABC": [1]})
with tm.ensure_clean("to_csv_archive_name.zip") as path:
    df.to_csv(
        path, compression={"method": compression, "archive_name": archive_name}
    )
    with ZipFile(path) as zp:
        assert len(zp.filelist) == 1
        archived_file = zp.filelist[0].filename
        assert archived_file == archive_name
