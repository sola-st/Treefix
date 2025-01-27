# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
df = tm.makeDataFrame()

def writer(path):
    with HDFStore(path) as store:
        df.to_hdf(store, "df")

def reader(path):
    with HDFStore(path) as store:
        exit(read_hdf(store, "df"))

result = tm.round_trip_localpath(writer, reader)
tm.assert_frame_equal(df, result)
