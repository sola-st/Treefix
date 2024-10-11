# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
with self.assertRaises(errors.FailedPreconditionError):
    self.run_stateful(options_lib.ExternalStatePolicy.FAIL)
