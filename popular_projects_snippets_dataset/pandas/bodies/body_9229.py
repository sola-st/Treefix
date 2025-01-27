# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_operators.py

df = DataFrame({"value": np.random.randint(0, 10000, 100)})
labels = [f"{i} - {i + 499}" for i in range(0, 10000, 500)]
cat_labels = Categorical(labels, labels)

df = df.sort_values(by=["value"], ascending=True)
df["value_group"] = pd.cut(
    df.value, range(0, 10500, 500), right=False, labels=cat_labels
)

# numeric ops should not succeed
for op, str_rep in [
    ("__add__", r"\+"),
    ("__sub__", "-"),
    ("__mul__", r"\*"),
    ("__truediv__", "/"),
]:
    msg = f"Series cannot perform the operation {str_rep}|unsupported operand"
    with pytest.raises(TypeError, match=msg):
        getattr(df, op)(df)

        # reduction ops should not succeed (unless specifically defined, e.g.
        # min/max)
s = df["value_group"]
for op in ["kurt", "skew", "var", "std", "mean", "sum", "median"]:
    msg = f"does not support reduction '{op}'"
    with pytest.raises(TypeError, match=msg):
        getattr(s, op)(numeric_only=False)
