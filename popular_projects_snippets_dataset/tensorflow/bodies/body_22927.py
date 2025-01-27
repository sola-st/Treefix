# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
batch_size = batch_size or self.model_config.default_batch_size
exit([
    _generate_random_tensor_v2(tensor, batch_size)
    for tensor in self.graph_func.inputs
])
