# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
super(TFRTypeResolver, self).__init__()
self._op_defs = op_defs

# This pattern matching mechanism works with the functional form generated
# by autograph:
#
#   for i in data:
#     print(i)
#
# generates:
#
#   def loop_body(itr):
#     i = itr
#     print(i)
#   ag__.for_stmt(target)
#
# The mechanism lets us infer the type of the itr argument based on that of
# target.
self._for_loop_target_types = {}  # Maps body function name to iterated.
self._for_loop_body_fns = {}  # Used only to avoid collisions.
