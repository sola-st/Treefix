# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
with tm.ensure_clean(filename=".foo") as file:
    pd.DataFrame(
        [["1", "2"]],
        columns=["foo", "bar"],
    ).to_csv(file, compression={"method": "tar", "mode": "w:gz"}, index=False)
    with gzip.open(file) as uncompressed:
        with tarfile.TarFile(fileobj=uncompressed) as archive:
            members = archive.getmembers()
            assert len(members) == 1
            content = archive.extractfile(members[0]).read().decode("utf8")

            if is_platform_windows():
                expected = "foo,bar\r\n1,2\r\n"
            else:
                expected = "foo,bar\n1,2\n"

            assert content == expected
