# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 30924
df = DataFrame({"col1": ["a", "b", "c"], "col2": [1, 2, 3], "col3": [1, 2, 3]})
msg = r"pivot\(\) missing 1 required argument: 'columns'"
with pytest.raises(TypeError, match=msg):
    df.pivot(index="col1", values="col3")
