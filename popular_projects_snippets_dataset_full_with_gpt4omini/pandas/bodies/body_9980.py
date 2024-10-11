# Extracted from ./data/repos/pandas/pandas/tests/window/test_base_indexer.py
# GH 43267
df = DataFrame(df_data)
num_trials = 3
indexer = indexer_class(window_size=window_size)
original_window_size = indexer.window_size
for i in range(num_trials):
    df.groupby("a")["b"].rolling(window=indexer, min_periods=1).mean()
    assert indexer.window_size == original_window_size
