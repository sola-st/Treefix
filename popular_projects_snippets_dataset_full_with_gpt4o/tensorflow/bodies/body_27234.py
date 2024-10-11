# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
worker_addresses = ["localhost:%port%"]
with self.assertRaisesRegex(
    RuntimeError,
    "other workers are already running at the configured host"):
    _ = _make_service_cluster(
        num_workers=5, local_shard_index=1, worker_addresses=worker_addresses)
