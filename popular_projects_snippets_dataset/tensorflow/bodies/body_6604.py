# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
batch_size = 8
dataset = dataset_ops.DatasetV2.from_tensor_slices({
    "feature": array_ops.ones([batch_size, 10]),
    "label": array_ops.ones([batch_size]),
})
dataset = dataset.batch(batch_size, drop_remainder=True)
dataset = dataset.repeat()
dist_dataset = distribution.experimental_distribute_dataset(dataset)
per_replica_batch_size = batch_size // distribution.num_replicas_in_sync

@def_function.function
def train_fn():
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

train_fn()
