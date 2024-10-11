# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    Convert to specific type of Manager. Does not copy if the type is already
    correct. Does not guarantee a copy otherwise. `copy` keyword only controls
    whether conversion from Block->ArrayManager copies the 1D arrays.
    """
new_mgr: Manager

if typ == "block":
    if isinstance(mgr, BlockManager):
        new_mgr = mgr
    else:
        if mgr.ndim == 2:
            new_mgr = arrays_to_mgr(
                mgr.arrays, mgr.axes[0], mgr.axes[1], typ="block"
            )
        else:
            new_mgr = SingleBlockManager.from_array(mgr.arrays[0], mgr.index)
elif typ == "array":
    if isinstance(mgr, ArrayManager):
        new_mgr = mgr
    else:
        if mgr.ndim == 2:
            arrays = [mgr.iget_values(i) for i in range(len(mgr.axes[0]))]
            if copy:
                arrays = [arr.copy() for arr in arrays]
            new_mgr = ArrayManager(arrays, [mgr.axes[1], mgr.axes[0]])
        else:
            array = mgr.internal_values()
            if copy:
                array = array.copy()
            new_mgr = SingleArrayManager([array], [mgr.index])
else:
    raise ValueError(f"'typ' needs to be one of {{'block', 'array'}}, got '{typ}'")
exit(new_mgr)
