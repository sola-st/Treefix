# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
super(DistributedIteratorTfDataServiceTest, self).setUp()
self.num_workers = 3
if combinations.in_main_process():
    self.dispatcher = server_lib.DispatchServer()
    self.workers = []
    for _ in range(self.num_workers):
        self.workers.append(
            server_lib.WorkerServer(
                server_lib.WorkerConfig(
                    dispatcher_address=self.dispatcher.target.split("://")[1],
                    heartbeat_interval_ms=100,
                    dispatcher_timeout_ms=1000)))
    combinations.env().tf_data_service_dispatcher = self.dispatcher.target
