# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
exit(math_ops.equal(self.replica_id_in_sync_group,
                      constant_op.constant(0)))
