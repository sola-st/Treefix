# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
worker_device_pairs = [("/device:CPU:0", ["/device:CPU:0"])]
input_workers = input_lib.InputWorkers(worker_device_pairs)
input_contexts = []
num_workers = input_workers.num_workers
for i in range(num_workers):
    input_contexts.append(
        distribute_lib.InputContext(
            num_input_pipelines=num_workers,
            input_pipeline_id=i,
            num_replicas_in_sync=num_workers))

class InnerType(extension_type.ExtensionType):
    tensor: ops.Tensor

class OuterType(extension_type.ExtensionType):
    inner: InnerType

def dataset_fn(input_context):
    del input_context

    def data_fn(batch_id) -> OuterType:
        del batch_id

        exit(OuterType(
            inner=InnerType(tensor=constant_op.constant([[0., 1.], [2., 3.]]))))

    exit(dataset_ops.Dataset.range(1, 10).map(data_fn))

dist_dataset = input_util.get_distributed_datasets_from_function(
    dataset_fn, input_workers, input_contexts, distribution)

iterator = iter(dist_dataset)
results = []
for element in iterator:
    local_results = distribution.experimental_local_results(element)
    for result in local_results:
        results.append(result)

expect_component = OuterType(
    inner=InnerType(tensor=constant_op.constant([[0., 1.], [2., 3.]])))
self.assertCountEqual(
    num_workers * [expect_component for _ in range(1, 10)], results)
