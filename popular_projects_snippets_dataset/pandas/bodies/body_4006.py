# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py

# test the dict methods
df = DataFrame(
    {
        "A": np.array(np.random.randn(6), dtype=np.float64),
        "A1": np.array(np.random.randn(6), dtype=np.float64),
        "B": np.array(np.arange(6), dtype=np.int64),
        "C": ["foo"] * 6,
        "D": np.array([True, False] * 3, dtype=bool),
        "E": np.array(np.random.randn(6), dtype=np.float32),
        "E1": np.array(np.random.randn(6), dtype=np.float32),
        "F": np.array(np.arange(6), dtype=np.int32),
    }
)

# columns is in a different order here than the actual items iterated
# from the dict
blocks = df._to_dict_of_blocks()
columns = []
for b in blocks.values():
    columns.extend(b.columns)

asdict = dict(df.items())
asdict2 = {x: y.values for x, y in df.items()}

# dict of series & dict of ndarrays (have dtype info)
results = []
results.append(DataFrame.from_records(asdict).reindex(columns=df.columns))
results.append(
    DataFrame.from_records(asdict, columns=columns).reindex(columns=df.columns)
)
results.append(
    DataFrame.from_records(asdict2, columns=columns).reindex(columns=df.columns)
)

for r in results:
    tm.assert_frame_equal(r, df)
