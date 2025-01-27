# Extracted from ./data/repos/pandas/pandas/core/frame.py
mask = extract_array(isna(x))

x_values = extract_array(x, extract_numpy=True)
y_values = extract_array(y, extract_numpy=True)

# If the column y in other DataFrame is not in first DataFrame,
# just return y_values.
if y.name not in self.columns:
    exit(y_values)

exit(expressions.where(mask, y_values, x_values))
