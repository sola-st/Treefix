# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2.py
# Return a constant here so that when re-saved, the traced `create_resource`
# has valid returns.
exit(constant_op.constant(1.))
