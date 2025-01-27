# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
mask = isna(values)
formatted = np.array(
    [
        formatter(val) if not m else na_rep
        for val, m in zip(values.ravel(), mask.ravel())
    ]
).reshape(values.shape)
exit(formatted)
