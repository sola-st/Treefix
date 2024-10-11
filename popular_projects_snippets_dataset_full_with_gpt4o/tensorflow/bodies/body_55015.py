# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
rt_checker = dispatch.MakeInstanceChecker(ragged_tensor.RaggedTensor)
tensor_checker = dispatch.MakeInstanceChecker(ops.Tensor)
rt_or_tensor = dispatch.MakeUnionChecker([rt_checker, tensor_checker])
checker = dispatch.PySignatureChecker([(0, rt_or_tensor),
                                       (1, rt_or_tensor)])

t = constant_op.constant([[1, 2], [3, 4]])
rt = ragged_factory_ops.constant([[1, 2], [3]])

self.check_signatures(checker, [
    ((t, t), False),
    ((t, rt), True),
    ((rt, t), True),
    ((rt, rt), True),
    ((rt, [rt]), False),
    ((rt, rt, 1, 2, None), True),
])  # pyformat: disable

self.assertEqual(
    repr(checker),
    '<PySignatureChecker args[0]:Union[RaggedTensor, Tensor], '
    'args[1]:Union[RaggedTensor, Tensor]>')
