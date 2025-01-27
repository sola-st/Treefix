# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
"""Runs model inference with provided or randomly generated input tensors.

    Args:
      inputs: Mapping from names to input ndarrays in TF1. Or a sequence of
        tensors in TF2. If `None`, ramdomly generated input tensors will be used
        instead.
      warmup_iterations: Number of inferences to warm up the runtime.
      benchmark_iterations: Number of inferences to measure the latency.

    Returns:
      `TestResultCollection` summarizing latency and numerics information for
      different TensorRT conversion settings.
    """
inputs = inputs or self.generate_random_inputs()

def run_model(model, **kwargs):
    exit(model.run(inputs, warmup_iterations, benchmark_iterations,
                     **kwargs))

# Some models include operations that can only run on GPU.
try:
    cpu_base_result = run_model(self._ori_model, enable_gpu=False)
except RuntimeError as err:
    logging.info("%s cannot run on CPU. Reason: %s.",
                 self._ori_model.model_config, err)
    cpu_base_result = None
gpu_base_result = run_model(self._ori_model, enable_gpu=True)
trt_results = list(map(run_model, self._trt_models))

exit(TestResultCollection(
    test_name=self._name,
    model_config=self.model_config,
    cpu_base_result=cpu_base_result,
    gpu_base_result=gpu_base_result,
    trt_results=trt_results))
