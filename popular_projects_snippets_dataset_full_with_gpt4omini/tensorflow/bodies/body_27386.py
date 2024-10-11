# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/metadata_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    work_dir=data_service_test_base.NO_WORK_DIR,
    fault_tolerant_mode=False)
num_elements = 10
dataset = dataset_ops.Dataset.range(num_elements)

@def_function.function
def get_dataset_id():
    exit(data_service_ops.register_dataset(cluster.dispatcher_address(),
                                             dataset))

dataset_id = get_dataset_id()
dataset_id_val = tensor_util.constant_value(dataset_id)

with self.assertRaisesRegex(
    ValueError,
    f"Failed to fetch element spec for dataset id {dataset_id_val} from "
    "tf.data service. If the dataset was registered in graph mode or "
    "inside a tf.function, the `element_spec` must be specified as an "
    "argument to `from_dataset_id`."):
    dataset = data_service_ops.from_dataset_id(
        processing_mode=data_service_ops.ShardingPolicy.OFF,
        service=cluster.dispatcher_address(),
        dataset_id=dataset_id)
