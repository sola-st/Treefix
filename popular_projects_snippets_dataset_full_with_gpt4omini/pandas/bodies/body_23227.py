# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py

# Check uniqueness of each
if self.left_index:
    left_unique = self.orig_left.index.is_unique
else:
    left_unique = MultiIndex.from_arrays(self.left_join_keys).is_unique

if self.right_index:
    right_unique = self.orig_right.index.is_unique
else:
    right_unique = MultiIndex.from_arrays(self.right_join_keys).is_unique

# Check data integrity
if validate in ["one_to_one", "1:1"]:
    if not left_unique and not right_unique:
        raise MergeError(
            "Merge keys are not unique in either left "
            "or right dataset; not a one-to-one merge"
        )
    if not left_unique:
        raise MergeError(
            "Merge keys are not unique in left dataset; not a one-to-one merge"
        )
    if not right_unique:
        raise MergeError(
            "Merge keys are not unique in right dataset; not a one-to-one merge"
        )

elif validate in ["one_to_many", "1:m"]:
    if not left_unique:
        raise MergeError(
            "Merge keys are not unique in left dataset; not a one-to-many merge"
        )

elif validate in ["many_to_one", "m:1"]:
    if not right_unique:
        raise MergeError(
            "Merge keys are not unique in right dataset; "
            "not a many-to-one merge"
        )

elif validate in ["many_to_many", "m:m"]:
    pass

else:
    raise ValueError(
        f'"{validate}" is not a valid argument. '
        "Valid arguments are:\n"
        '- "1:1"\n'
        '- "1:m"\n'
        '- "m:1"\n'
        '- "m:m"\n'
        '- "one_to_one"\n'
        '- "one_to_many"\n'
        '- "many_to_one"\n'
        '- "many_to_many"'
    )
