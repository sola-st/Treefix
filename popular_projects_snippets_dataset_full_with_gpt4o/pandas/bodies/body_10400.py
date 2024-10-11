# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# case that goes through _transform_item_by_item

df.columns = ["A", "B", "B", "D"]

# this also tests orderings in transform between
# series/frame to make sure it's consistent
grouped = df.groupby("A")

gbc = grouped["B"]
with pytest.raises(TypeError, match="Could not convert"):
    gbc.transform(lambda x: np.mean(x))

with pytest.raises(TypeError, match="Could not convert"):
    df.groupby("A").transform(lambda x: np.mean(x))
