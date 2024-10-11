# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
worker_addresses = [f"fake_worker_{i}" for i in range(5)]
with self.assertRaisesRegex(RuntimeError,
                            "The worker's address is not configured"):
    _ = _make_service_cluster(
        num_workers=5, local_shard_index=0, worker_addresses=worker_addresses)
