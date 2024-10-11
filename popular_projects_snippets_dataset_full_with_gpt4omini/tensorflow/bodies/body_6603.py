# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
data = iter(dist_dataset).get_next_as_optional().get_value()
data = nest.map_structure(distribution.experimental_local_results, data)
feature = data["feature"]
label = data["label"]

# Assert the shapes are still static from all replicas.
for replica_id in range(len(distribution.extended.worker_devices)):
    self.assertEqual([per_replica_batch_size, 10],
                     feature[replica_id].shape.as_list())
    self.assertEqual([per_replica_batch_size],
                     label[replica_id].shape.as_list())
