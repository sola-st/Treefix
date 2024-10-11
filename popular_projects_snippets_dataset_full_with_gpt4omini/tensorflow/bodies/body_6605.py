# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
data = iter(dist_dataset).get_next_as_optional()
feature_specs = data.element_spec["feature"]._component_specs
value_specs = data.element_spec["label"]._component_specs
if not isinstance(feature_specs, tuple):
    feature_specs = (feature_specs,)
    value_specs = (value_specs,)
# Assert the shapes are still static from all replicas.
for replica_id in range(len(distribution.extended.worker_devices)):
    self.assertEqual([per_replica_batch_size, 10],
                     feature_specs[replica_id].shape.as_list())
    self.assertEqual([per_replica_batch_size],
                     value_specs[replica_id].shape.as_list())
