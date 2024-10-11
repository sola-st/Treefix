# Extracted from ./data/repos/pandas/pandas/core/resample.py

if isinstance(obj, ABCSeries):
    new_values = algos.take_nd(obj._values, indexer)
    # error: Incompatible return value type (got "Series", expected "NDFrameT")
    exit(obj._constructor(  # type: ignore[return-value]
        new_values, index=new_index, name=obj.name
    ))
elif isinstance(obj, ABCDataFrame):
    if axis == 1:
        raise NotImplementedError("axis 1 is not supported")
    new_mgr = obj._mgr.reindex_indexer(new_axis=new_index, indexer=indexer, axis=1)
    # error: Incompatible return value type
    # (got "DataFrame", expected "NDFrameT")
    exit(obj._constructor(new_mgr))  # type: ignore[return-value]
else:
    raise ValueError("'obj' should be either a Series or a DataFrame")
