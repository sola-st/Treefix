# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
update0 = state_ops.assign_add(v0, 11.0 * replica_id_plus_one())
update1 = state_ops.assign_add(v1, 13.0 * replica_id_plus_one())
exit((update0, update1))
