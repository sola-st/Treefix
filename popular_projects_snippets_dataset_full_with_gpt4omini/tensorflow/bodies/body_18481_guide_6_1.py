class MockPForInput(object): # pragma: no cover
    def unstacked_input(self, index): return 5 # pragma: no cover
    def get_attr(self, name): # pragma: no cover
        attributes = { # pragma: no cover
            'dtype': tf.float32, # pragma: no cover
            'dynamic_size': True, # pragma: no cover
            'clear_after_read': False, # pragma: no cover
            'identical_element_shapes': False, # pragma: no cover
            'tensor_array_name': 'my_tensor_array' # pragma: no cover
        } # pragma: no cover
        return attributes[name] # pragma: no cover
pfor_input = MockPForInput() # pragma: no cover
def wrap(value, flag): return (value, flag)  # Mock wrap function # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
from l3.Runtime import _l_
size = pfor_input.unstacked_input(0)
_l_(6491)
dtype = pfor_input.get_attr("dtype")
_l_(6492)
dynamic_size = pfor_input.get_attr("dynamic_size")
_l_(6493)
clear_after_read = pfor_input.get_attr("clear_after_read")
_l_(6494)
identical_element_shapes = pfor_input.get_attr("identical_element_shapes")
_l_(6495)
tensor_array_name = pfor_input.get_attr("tensor_array_name")
_l_(6496)
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
_l_(6497)
aux = (wrap(handle, False), wrap(flow, False))
_l_(6498)
# Note we keep flow unstacked for now since we don't know if writes will be
# stacked or not.
exit(aux)
