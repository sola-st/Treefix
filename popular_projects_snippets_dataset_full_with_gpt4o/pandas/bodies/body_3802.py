# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
# GH 46622
# Dups on left allowed by many_to_one constraint
left_w_dups.join(
    right_no_dup,
    on="a",
    validate="many_to_one",
)

# Dups on left not allowed by one_to_one constraint
msg = "Merge keys are not unique in left dataset; not a one-to-one merge"
with pytest.raises(MergeError, match=msg):
    left_w_dups.join(
        right_no_dup,
        on="a",
        validate="one_to_one",
    )
