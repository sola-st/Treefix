# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
rt_checker = dispatch.MakeInstanceChecker(ragged_tensor.RaggedTensor)
rt_list_checker = dispatch.MakeListChecker(rt_checker)
checker = dispatch.PySignatureChecker([(0, rt_list_checker)])

rt = ragged_factory_ops.constant([[1, 2], [3]])

self.check_signatures(checker, [
    (([rt],), True),
    (([],), False),
    ((rt,), False),
    (([rt, rt+3, rt*2],), True),
    (([rt, rt.values, rt*2],), False),
])  # pyformat: disable

self.assertEqual(
    repr(checker), '<PySignatureChecker args[0]:List[RaggedTensor]>')
