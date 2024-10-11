# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
_left = _validate_operand(left)
_right = _validate_operand(right)
self.left = self.orig_left = _left
self.right = self.orig_right = _right
self.how = how

# bm_axis -> the axis on the BlockManager
self.bm_axis = axis
# axis --> the axis on the Series/DataFrame
self.axis = 1 - axis if self.left.ndim == 2 else 0

self.on = com.maybe_make_list(on)

self.suffixes = suffixes
self.sort = sort

self.left_index = left_index
self.right_index = right_index

self.indicator = indicator

if not is_bool(left_index):
    raise ValueError(
        f"left_index parameter must be of type bool, not {type(left_index)}"
    )
if not is_bool(right_index):
    raise ValueError(
        f"right_index parameter must be of type bool, not {type(right_index)}"
    )

# GH 40993: raise when merging between different levels; enforced in 2.0
if _left.columns.nlevels != _right.columns.nlevels:
    msg = (
        "Not allowed to merge between different levels. "
        f"({_left.columns.nlevels} levels on the left, "
        f"{_right.columns.nlevels} on the right)"
    )
    raise MergeError(msg)

self.left_on, self.right_on = self._validate_left_right_on(left_on, right_on)

cross_col = None
if self.how == "cross":
    (
        self.left,
        self.right,
        self.how,
        cross_col,
    ) = self._create_cross_configuration(self.left, self.right)
    self.left_on = self.right_on = [cross_col]
self._cross = cross_col

# note this function has side effects
(
    self.left_join_keys,
    self.right_join_keys,
    self.join_names,
) = self._get_merge_keys()

# validate the merge keys dtypes. We may need to coerce
# to avoid incompatible dtypes
self._maybe_coerce_merge_keys()

# If argument passed to validate,
# check if columns specified as unique
# are in fact unique.
if validate is not None:
    self._validate(validate)
