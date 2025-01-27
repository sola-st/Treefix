# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
int_checker = dispatch.MakeInstanceChecker(int)
rt_checker = dispatch.MakeInstanceChecker(ragged_tensor.RaggedTensor)
checker = dispatch.PySignatureChecker([(0, int_checker), (2, rt_checker)])
rt = ragged_factory_ops.constant([[1, 2], [3]])

self.check_signatures(checker, [
    ((1, 2, rt), True),
    ((1, 2, 3), False),
    ((1, 2), False), ((), False),
    ((5, 'x', rt, None), True),
    (([5], 'x', rt, None), False),
    ((5, 'x', [rt], None), False),
])  # pyformat: disable

self.assertEqual(
    repr(checker), '<PySignatureChecker args[0]:int, args[2]:RaggedTensor>')
