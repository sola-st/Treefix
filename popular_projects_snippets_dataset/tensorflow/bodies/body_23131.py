# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Gets a single test method based on the parameters."""

def _Test(self):
    logging.info(f"Running test `{run_params.test_name}` with parameters: "
                 f"convert_online={run_params.convert_online}, "
                 f"precision_mode={run_params.precision_mode}, "
                 f"dynamic_engine={run_params.dynamic_engine}, "
                 f"dynamic_shape={run_params.dynamic_shape}")
    self.RunTest(run_params)

exit(_Test)
