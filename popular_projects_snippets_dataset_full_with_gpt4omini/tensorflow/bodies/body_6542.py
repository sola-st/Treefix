# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
update0 = v0.assign_add(5.0 * replica_id_plus_one())
update1 = v1.assign_add(7.0 * replica_id_plus_one())
exit((update0, update1))
