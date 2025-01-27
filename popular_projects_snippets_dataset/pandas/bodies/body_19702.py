# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
if downcast is False:
    exit(blocks)

if self.dtype == _dtype_obj:
    # GH#44241 We downcast regardless of the argument;
    #  respecting 'downcast=None' may be worthwhile at some point,
    #  but ATM it breaks too much existing code.
    # split and convert the blocks

    exit(extend_blocks([blk.convert() for blk in blocks]))

if downcast is None:
    exit(blocks)

exit(extend_blocks([b._downcast_2d(downcast) for b in blocks]))
