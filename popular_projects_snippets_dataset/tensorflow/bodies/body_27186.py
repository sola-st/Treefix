# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_process_cluster.py
if port == 0:
    port = test_util.pick_unused_port()
self._dispatcher = server_lib.DispatchServer(
    service_config_pb2.DispatcherConfig(
        port=port,
        protocol="grpc",
        work_dir=self._work_dir,
        fault_tolerant_mode=True,
        worker_addresses=worker_addresses,
        deployment_mode=self._deployment_mode),
    start=True)
