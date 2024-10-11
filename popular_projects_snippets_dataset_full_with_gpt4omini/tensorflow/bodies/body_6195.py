# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
exit((("tf.distribute.ValueContext(replica id {}, "
         " total replicas in sync: ""{})")
        .format(self.replica_id_in_sync_group, self.num_replicas_in_sync)))
