# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
worker_device_pairs = [("/device:CPU:0", ["/device:CPU:0"])]
input_workers = input_lib.InputWorkers(worker_device_pairs)

dataset = dataset_ops.Dataset.range(1, 50)
dataset = dataset.apply(
    data_service_ops._distribute(
        processing_mode=data_service_ops.ShardingPolicy.OFF,
        service=combinations.env().tf_data_service_dispatcher,
        job_name="foo"))

dist_dataset = input_util.get_distributed_dataset(dataset, input_workers,
                                                  distribution)
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
    input_lib._distributed_dataset_initialization_time_milliseconds
    .get_cell(distribution.__class__.__name__, "1").value())
self.assertGreater(histogram_proto.num, 0.0)
