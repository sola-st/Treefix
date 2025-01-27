# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
worker_device_pairs = [("/device:CPU:0", ["/device:CPU:0"])]
input_workers = input_lib.InputWorkers(worker_device_pairs)
input_contexts = []
num_workers = input_workers.num_workers
for i in range(num_workers):
    input_contexts.append(distribute_lib.InputContext(
        num_input_pipelines=num_workers,
        input_pipeline_id=i,
        num_replicas_in_sync=num_workers))

dataset = dataset_ops.Dataset.range(1, 50)
dataset_id = data_service_ops.register_dataset(
    service=combinations.env().tf_data_service_dispatcher,
    dataset=dataset)

def dataset_fn(input_context):
    del input_context
    exit(data_service_ops.from_dataset_id(
        processing_mode=data_service_ops.ShardingPolicy.OFF,
        service=combinations.env().tf_data_service_dispatcher,
        dataset_id=dataset_id,
        element_spec=dataset.element_spec,
        job_name="shared_job"))

dist_dataset = input_util.get_distributed_datasets_from_function(
    dataset_fn, input_workers, input_contexts, distribution)

iterator = iter(dist_dataset)
results = []
for element in iterator:
    local_results = distribution.experimental_local_results(element)
    for result in local_results:
        # input_lib.distributed_dataset may add extra '0' elements to pad
        # per-replica results.
        if result.numpy() != 0:
            results.append(result.numpy())
self.assertNotEmpty(results)
gathered = distribution.gather(constant_op.constant(results), axis=0)
self.assertCountEqual(self.num_workers * list(range(1, 50)), gathered)
histogram_proto = (
    input_lib
    ._distributed_dataset_from_function_initialization_time_milliseconds
    .get_cell(distribution.__class__.__name__, "1").value())
self.assertGreater(histogram_proto.num, 0.0)
