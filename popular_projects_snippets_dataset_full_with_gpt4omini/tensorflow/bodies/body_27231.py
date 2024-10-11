# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
with self.assertRaisesRegex(RuntimeError,
                            "The worker's address is not configured"):
    _ = _make_service_cluster(
        num_workers=5,
        local_shard_index=0,
        worker_addresses=["localhost:worker" for _ in range(5)])
