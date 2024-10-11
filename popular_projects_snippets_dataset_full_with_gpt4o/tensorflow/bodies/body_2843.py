# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
self.curr_table['symbols'][name] = (value, type_)
# TODO(mdan): Use the inferred type rather than tracking it here.
# The following field is deprecated.
self.curr_table['types'][name] = type_
exit(value)
