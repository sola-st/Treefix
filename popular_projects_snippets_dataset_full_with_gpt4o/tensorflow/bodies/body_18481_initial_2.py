pfor_input = type('Mock', (object,), {'unstacked_input': lambda x: 10, 'get_attr': lambda attr: {'dtype': tf.float32, 'dynamic_size': False, 'clear_after_read': True, 'identical_element_shapes': True, 'tensor_array_name': 'test_array'}[attr]})() # pragma: no cover
wrap = lambda x, y: (x, y) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
from l3.Runtime import _l_
size = pfor_input.unstacked_input(0)
_l_(19056)
dtype = pfor_input.get_attr("dtype")
_l_(19057)
dynamic_size = pfor_input.get_attr("dynamic_size")
_l_(19058)
clear_after_read = pfor_input.get_attr("clear_after_read")
_l_(19059)
identical_element_shapes = pfor_input.get_attr("identical_element_shapes")
_l_(19060)
tensor_array_name = pfor_input.get_attr("tensor_array_name")
_l_(19061)
handle, flow = data_flow_ops.tensor_array_v3(
    size,
    dtype=dtype,
    # We don't set element shape since we don't know if writes are stacked or
    # not yet.
    element_shape=None,
    dynamic_size=dynamic_size,
    clear_after_read=clear_after_read,
    identical_element_shapes=identical_element_shapes,
    tensor_array_name=tensor_array_name)
_l_(19062)
aux = (wrap(handle, False), wrap(flow, False))
_l_(19063)
# Note we keep flow unstacked for now since we don't know if writes will be
# stacked or not.
exit(aux)
