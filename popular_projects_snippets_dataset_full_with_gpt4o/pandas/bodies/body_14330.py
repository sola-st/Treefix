# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
path = tmp_path / setup_path
df = DataFrame({"a": [1]})

with HDFStore(path, mode="w") as hdf:
    hdf.put(
        "table",
        df,
        format="table",
        data_columns=True,
        index=None,
        track_times=track_times,
    )

exit(checksum(path))
