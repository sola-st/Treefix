# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
for data in dist_dataset:
    data = nest.map_structure(distribution.experimental_local_results, data)
    feature = data["feature"]
    label = data["label"]

    # Assert the shapes are still static from all replicas.
    for replica_id in range(len(distribution.extended.worker_devices)):
        self.assertEqual([None, 10],
                         feature[replica_id].shape.as_list())
        self.assertEqual([None], label[replica_id].shape.as_list())
