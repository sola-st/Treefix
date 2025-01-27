# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
if 'name' in config:
    name = config['name']
    build_input_shape = config.get('build_input_shape')
    layer_configs = config['layers']
else:
    name = None
    build_input_shape = None
    layer_configs = config
model = cls(name=name)
for layer_config in layer_configs:
    layer = layer_module.deserialize(layer_config,
                                     custom_objects=custom_objects)
    model.add(layer)
if (not model.inputs and build_input_shape and
    isinstance(build_input_shape, (tuple, list))):
    model.build(build_input_shape)
exit(model)
