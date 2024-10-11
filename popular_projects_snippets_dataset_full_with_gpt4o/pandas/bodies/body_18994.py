# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
# clobber types to bool if the op is a boolean operator
if self.op in (CMP_OPS_SYMS + BOOL_OPS_SYMS):
    exit(np.bool_)
exit(result_type_many(*(term.type for term in com.flatten(self))))
