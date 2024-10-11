class MockPForInput:# pragma: no cover
    def unstacked_input(self, index):# pragma: no cover
        return 10# pragma: no cover
    def get_attr(self, name):# pragma: no cover
        return {'dtype': tf.float32, 'dynamic_size': True, 'clear_after_read': False, 'identical_element_shapes': True, 'tensor_array_name': 'my_tensor_array'}[name]# pragma: no cover
# pragma: no cover
pfor_input = MockPForInput() # pragma: no cover
class MockDataFlowOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def tensor_array_v3(size, dtype, element_shape, dynamic_size, clear_after_read, identical_element_shapes, tensor_array_name):# pragma: no cover
        return ('handle', 'flow')# pragma: no cover
# pragma: no cover
data_flow_ops = MockDataFlowOps() # pragma: no cover
def mock_wrap(value, flag):# pragma: no cover
    return {'value': value, 'flag': flag}# pragma: no cover
# pragma: no cover
wrap = mock_wrap # pragma: no cover

class MockPForInput:# pragma: no cover
    def unstacked_input(self, index):# pragma: no cover
        return 10# pragma: no cover
    def get_attr(self, name):# pragma: no cover
        if name == 'dtype':# pragma: no cover
            return tf.float32# pragma: no cover
        elif name == 'dynamic_size':# pragma: no cover
            return True# pragma: no cover
        elif name == 'clear_after_read':# pragma: no cover
            return False# pragma: no cover
        elif name == 'identical_element_shapes':# pragma: no cover
            return True# pragma: no cover
        elif name == 'tensor_array_name':# pragma: no cover
            return 'my_tensor_array'# pragma: no cover
        return None# pragma: no cover
# pragma: no cover
pfor_input = MockPForInput() # pragma: no cover
class MockDataFlowOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def tensor_array_v3(size, dtype, element_shape, dynamic_size, clear_after_read, identical_element_shapes, tensor_array_name):# pragma: no cover
        return ('handle', 'flow')# pragma: no cover
# pragma: no cover
data_flow_ops = MockDataFlowOps() # pragma: no cover
def wrap(value, flag):# pragma: no cover
    return (value, flag) # pragma: no cover

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
