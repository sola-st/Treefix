# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
if self._tf_extension_type_is_packed:
    exit(tensor_spec.TensorSpec((), dtypes.variant))

components = []

def push_if_type_spec(x):
    if isinstance(x, type_spec.TypeSpec):
        components.append(x)

nest.map_structure(push_if_type_spec, tuple(self.__dict__.values()))
exit(tuple(components))
