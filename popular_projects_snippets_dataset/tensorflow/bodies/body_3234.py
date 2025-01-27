# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/concurrency_test.py
# Ensure that multiple conversion jobs with calibration won't encounter any
# concurrency issue.
with self.pool:
    jobs = []
    for _ in range(10):
        jobs.append(self.pool.submit(self._convert_with_calibration))

    for job in jobs:
        self.assertIsNotNone(job.result())
