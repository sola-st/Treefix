# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
# GH 46622
# Dups on right allowed by one_to_many constraint
left_no_dup.join(
    right_w_dups,
    on="a",
    validate="one_to_many",
)

# Dups on right not allowed by one_to_one constraint
msg = "Merge keys are not unique in right dataset; not a one-to-one merge"
with pytest.raises(MergeError, match=msg):
    left_no_dup.join(
        right_w_dups,
        on="a",
        validate="one_to_one",
    )
