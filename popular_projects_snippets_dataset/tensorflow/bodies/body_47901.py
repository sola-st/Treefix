# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
config = config.copy()
function = cls._parse_function_from_config(
    config, custom_objects, 'function', 'module', 'function_type')

output_shape = cls._parse_function_from_config(
    config, custom_objects, 'output_shape', 'output_shape_module',
    'output_shape_type')
if 'mask' in config:
    mask = cls._parse_function_from_config(
        config, custom_objects, 'mask', 'mask_module', 'mask_type')
else:
    mask = None

config['function'] = function
config['output_shape'] = output_shape
config['mask'] = mask

# If arguments were numpy array, they have been saved as
# list. We need to recover the ndarray
if 'arguments' in config:
    for key in config['arguments']:
        if isinstance(config['arguments'][key], dict):
            arg_dict = config['arguments'][key]
            if 'type' in arg_dict and arg_dict['type'] == 'ndarray':
                # Overwrite the argument with its numpy translation
                config['arguments'][key] = np.array(arg_dict['value'])

exit(cls(**config))
