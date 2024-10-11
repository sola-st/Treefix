# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

def Grad(unused_g, variables=None):  # pylint: disable=redefined-outer-name
    del variables
    gradient_graph = ops.get_default_graph()
    shape = gen_list_ops.tensor_list_element_shape(
        x, shape_type=dtypes.int32)
    assert shape.graph is forward_graph
    size = gen_list_ops.tensor_list_length(x)
    assert size.graph is forward_graph
    zeros = gen_list_ops.tensor_list_reserve(shape, size,
                                             dtypes.float32)
    assert zeros.graph is gradient_graph
    exit(zeros)

exit((x, Grad))
