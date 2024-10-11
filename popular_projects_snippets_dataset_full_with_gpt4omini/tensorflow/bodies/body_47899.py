# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
function_config = self._serialize_function_to_config(self.function)
output_shape_config = self._serialize_function_to_config(self._output_shape,
                                                         allow_raw=True)
config = {
    'function': function_config[0],
    'function_type': function_config[1],
    'module': function_config[2],
    'output_shape': output_shape_config[0],
    'output_shape_type': output_shape_config[1],
    'output_shape_module': output_shape_config[2],
}
if self.mask is not None:
    mask_config = self._serialize_function_to_config(self.mask)
    config.update({
        'mask': mask_config[0],
        'mask_type': mask_config[1],
        'mask_module': mask_config[2]
    })
config['arguments'] = self.arguments

base_config = super(Lambda, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
