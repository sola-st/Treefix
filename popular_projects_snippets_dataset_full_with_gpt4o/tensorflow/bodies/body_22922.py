# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
batch_size = batch_size or self.model_config.default_batch_size
exit({
    tensor_info.name: _generate_random_tensor_v1(tensor_info, batch_size)
    for tensor_info in self.input_tensor_info.values()
})
