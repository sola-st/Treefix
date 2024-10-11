# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
# This test has side effects and can disrupt other tests, even if the
# resource created by it will not be used in following tests.
# TODO(b/155209534): enable this test.
# self.testPSPreemptionErrorType()

self.thread_coord = thread_coordinator.Coordinator(
    clean_stop_exception_types=[])
self.testWorkerPreemptionMidstFunction()

self.thread_coord = thread_coordinator.Coordinator(
    clean_stop_exception_types=[])
self.testWorkerPreemptionErrorType()
