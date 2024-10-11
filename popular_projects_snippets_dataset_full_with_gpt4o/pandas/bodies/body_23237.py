# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py

# note this function has side effects
(left_join_keys, right_join_keys, join_names) = super()._get_merge_keys()

# validate index types are the same
for i, (lk, rk) in enumerate(zip(left_join_keys, right_join_keys)):
    if not is_dtype_equal(lk.dtype, rk.dtype):
        if is_categorical_dtype(lk.dtype) and is_categorical_dtype(rk.dtype):
            # The generic error message is confusing for categoricals.
            #
            # In this function, the join keys include both the original
            # ones of the merge_asof() call, and also the keys passed
            # to its by= argument. Unordered but equal categories
            # are not supported for the former, but will fail
            # later with a ValueError, so we don't *need* to check
            # for them here.
            msg = (
                f"incompatible merge keys [{i}] {repr(lk.dtype)} and "
                f"{repr(rk.dtype)}, both sides category, but not equal ones"
            )
        else:
            msg = (
                f"incompatible merge keys [{i}] {repr(lk.dtype)} and "
                f"{repr(rk.dtype)}, must be the same type"
            )
        raise MergeError(msg)

        # validate tolerance; datetime.timedelta or Timedelta if we have a DTI
if self.tolerance is not None:

    if self.left_index:
        # Actually more specifically an Index
        lt = cast(AnyArrayLike, self.left.index)
    else:
        lt = left_join_keys[-1]

    msg = (
        f"incompatible tolerance {self.tolerance}, must be compat "
        f"with type {repr(lt.dtype)}"
    )

    if needs_i8_conversion(lt):
        if not isinstance(self.tolerance, datetime.timedelta):
            raise MergeError(msg)
        if self.tolerance < Timedelta(0):
            raise MergeError("tolerance must be positive")

    elif is_integer_dtype(lt):
        if not is_integer(self.tolerance):
            raise MergeError(msg)
        if self.tolerance < 0:
            raise MergeError("tolerance must be positive")

    elif is_float_dtype(lt):
        if not is_number(self.tolerance):
            raise MergeError(msg)
        if self.tolerance < 0:
            raise MergeError("tolerance must be positive")

    else:
        raise MergeError("key must be integer, timestamp or float")

        # validate allow_exact_matches
if not is_bool(self.allow_exact_matches):
    msg = (
        "allow_exact_matches must be boolean, "
        f"passed {self.allow_exact_matches}"
    )
    raise MergeError(msg)

exit((left_join_keys, right_join_keys, join_names))
