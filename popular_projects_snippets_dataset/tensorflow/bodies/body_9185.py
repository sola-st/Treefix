# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/integration_test/profiler_api_test.py
"""Test single worker sampling mode with a short delay.

    Expect that requested delayed start time will arrive late, and a subsequent
    retry will issue an immediate start.
    """

self.test_single_worker_sampling_mode(delay_ms=1)
