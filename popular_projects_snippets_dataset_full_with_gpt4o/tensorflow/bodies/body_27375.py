# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = data_service_test_base.TestCluster(num_workers=0)
for _ in range(num_workers):
    worker = data_service_test_base.TestWorker(
        dispatcher_address=cluster.dispatcher_address(),
        shutdown_quiet_period_ms=0,
        cross_trainer_cache_size_bytes=cross_trainer_cache_size_bytes)
    worker.start()
    cluster.workers.append(worker)
exit(cluster)
