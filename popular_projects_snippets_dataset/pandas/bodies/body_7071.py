# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py
# GH 10039
# set ops (+/-) raise TypeError
idx = Index(Categorical(["a", "b"]))
cat_or_list = "'(Categorical|list)' and '(Categorical|list)'"
msg = "|".join(
    [
        f"cannot perform {op_name} with this index type: CategoricalIndex",
        "can only concatenate list",
        rf"unsupported operand type\(s\) for [\+-]: {cat_or_list}",
    ]
)
with pytest.raises(TypeError, match=msg):
    func(idx)
