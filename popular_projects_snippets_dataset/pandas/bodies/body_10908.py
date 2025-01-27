# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
# Test gives the same results as grouped head and tail
n_groups = 100
n_rows_per_group = 30

data = {
    "group": [
        f"group {g}" for j in range(n_rows_per_group) for g in range(n_groups)
    ],
    "value": [
        f"group {g} row {j}"
        for j in range(n_rows_per_group)
        for g in range(n_groups)
    ],
}
df = pd.DataFrame(data)
grouped = df.groupby("group", as_index=False)
size = arg if arg >= 0 else n_rows_per_group + arg

if method == "head":
    result = grouped._positional_selector[:arg]

    if simulated:
        indices = []
        for j in range(size):
            for i in range(n_groups):
                if j * n_groups + i < n_groups * n_rows_per_group:
                    indices.append(j * n_groups + i)

        expected = df.iloc[indices]

    else:
        expected = grouped.head(arg)

else:
    result = grouped._positional_selector[-arg:]

    if simulated:
        indices = []
        for j in range(size):
            for i in range(n_groups):
                if (n_rows_per_group + j - size) * n_groups + i >= 0:
                    indices.append((n_rows_per_group + j - size) * n_groups + i)

        expected = df.iloc[indices]

    else:
        expected = grouped.tail(arg)

tm.assert_frame_equal(result, expected)
