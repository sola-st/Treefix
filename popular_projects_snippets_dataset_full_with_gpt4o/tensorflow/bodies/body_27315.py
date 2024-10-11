# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
dispatcher = server_lib.DispatchServer(
    service_config_pb2.DispatcherConfig(
        protocol="grpc",
        job_gc_check_interval_ms=50,
        job_gc_timeout_ms=20,
        client_timeout_ms=50))
dispatcher_address = dispatcher.target.split("://")[1]
_ = server_lib.WorkerServer(
    server_lib.WorkerConfig(
        dispatcher_address=dispatcher_address,
        heartbeat_interval_ms=100,
        data_transfer_protocol=self._get_data_transfer_protocol()))

num_elements = 1000
dataset = dataset_ops.Dataset.range(num_elements)
dataset = dataset.apply(
    data_service_ops._distribute(
        processing_mode=data_service_ops.ShardingPolicy.OFF,
        service=dispatcher.target,
        data_transfer_protocol=self._get_data_transfer_protocol(),
        task_refresh_interval_hint_ms=10000))
get_next = self.getNext(dataset)

# The client does not heartbeat in 10 seconds. It will be garbage-collected.
with self.assertRaisesRegex(errors.NotFoundError,
                            "Unknown iteration client id"):
    self.evaluate(get_next())
    time.sleep(3)
    self.getIteratorOutput(get_next)
