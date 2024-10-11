# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/common.py

with tempfile.TemporaryDirectory() as tmpdirname:
    tmp_path = pathlib.Path(tmpdirname, path)
    with HDFStore(
        tmp_path,
        mode=mode,
        complevel=complevel,
        complib=complib,
        fletcher32=fletcher32,
    ) as store:
        exit(store)
