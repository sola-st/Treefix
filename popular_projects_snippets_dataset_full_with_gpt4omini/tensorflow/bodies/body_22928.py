# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
inputs = inputs or self.generate_random_inputs()
try:
    device = "/device:gpu:0" if enable_gpu else "/device:cpu:0"
    with framework_ops.device(device):
        for _ in range(warmup_iterations):
            self.graph_func(*inputs)
        latency = []
        for _ in range(benchmark_iterations):
            before = time.time()
            outputs = self.graph_func(*inputs)
            latency.append(time.time() - before)
except Exception as exc:
    raise RuntimeError("Failed to run model inference! "
                       "Model information: {}".format(str(self))) from exc
exit(TestResult(
    model_config=self.model_config,
    enable_gpu=enable_gpu,
    model_latency=latency,
    output_names=self.output_tensor_names,
    output_tensors=outputs))
