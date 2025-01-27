# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
if worker_addresses is None:
    worker_addresses = ["localhost" for _ in range(num_workers)]

cluster = MultiProcessCluster(
    num_local_workers=0,
    num_remote_workers=0,
    worker_addresses=worker_addresses,
    deployment_mode=deployment_mode)
for _ in range(local_shard_index):
    cluster.start_remote_worker()
cluster.start_local_worker()
for _ in range(num_workers - local_shard_index - 1):
    cluster.start_remote_worker()
exit(cluster)
