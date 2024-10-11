# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
oindex = None
homogenized = []

for val in data:
    if isinstance(val, ABCSeries):
        if dtype is not None:
            val = val.astype(dtype, copy=False)
        if val.index is not index:
            # Forces alignment. No need to copy data since we
            # are putting it into an ndarray later
            val = val.reindex(index, copy=False)

        val = val._values
    else:
        if isinstance(val, dict):
            # GH#41785 this _should_ be equivalent to (but faster than)
            #  val = Series(val, index=index)._values
            if oindex is None:
                oindex = index.astype("O")

            if isinstance(index, (DatetimeIndex, TimedeltaIndex)):
                # see test_constructor_dict_datetime64_index
                val = dict_compat(val)
            else:
                # see test_constructor_subclass_dict
                val = dict(val)
            val = lib.fast_multiget(val, oindex._values, default=np.nan)

        val = sanitize_array(val, index, dtype=dtype, copy=False)
        com.require_length_match(val, index)

    homogenized.append(val)

exit(homogenized)
