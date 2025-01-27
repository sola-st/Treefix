# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# https://github.com/pandas-dev/pandas/issues/47172

labels = [f"c{i}" for i in range(10)]
df = DataFrame({col: np.zeros(len(labels)) for col in labels}, index=labels)
values = df._mgr.blocks[0].values

for label in df.columns:
    df[label][label] = 1

if not using_copy_on_write:
    # diagonal values all updated
    assert np.all(values[np.arange(10), np.arange(10)] == 1)
else:
    # original dataframe not updated
    assert np.all(values[np.arange(10), np.arange(10)] == 0)
