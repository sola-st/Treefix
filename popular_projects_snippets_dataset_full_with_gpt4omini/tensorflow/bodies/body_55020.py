# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
dispatcher = dispatch.PythonAPIDispatcher('tf.foo', ['x', 'ys', 'name'],
                                          (None,))

rt_checker = dispatch.MakeInstanceChecker(ragged_tensor.RaggedTensor)
tensor_checker = dispatch.MakeInstanceChecker(ops.Tensor)
rt_or_t = dispatch.MakeUnionChecker([rt_checker, tensor_checker])
list_of_rt_or_t = dispatch.MakeListChecker(rt_or_t)
f1 = lambda x, ys, name=None: 'f1'
dispatcher.Register(
    dispatch.PySignatureChecker([(0, rt_or_t), (1, list_of_rt_or_t)]), f1)

rt = ragged_factory_ops.constant([[1, 2], [3]])
t = constant_op.constant(5)
self.assertEqual(dispatcher.Dispatch((rt, [t]), None), 'f1')
self.assertEqual(dispatcher.Dispatch((rt, [rt]), None), 'f1')
self.assertEqual(dispatcher.Dispatch((t, [rt]), None), 'f1')
self.assertEqual(dispatcher.Dispatch((rt, []), None), 'f1')
self.assertEqual(dispatcher.Dispatch((t, [t, t, rt, t]), None), 'f1')
self.assertEqual(dispatcher.Dispatch((rt, [t], 'my_name'), None), 'f1')
self.assertEqual(dispatcher.Dispatch((), {'x': rt, 'ys': [t]}), 'f1')
self.assertEqual(
    dispatcher.Dispatch((), {
        'x': rt,
        'ys': [t],
        'name': 'x'
    }), 'f1')
self.assertEqual(dispatcher.Dispatch((t, [t]), None), NotImplemented)
self.assertEqual(dispatcher.Dispatch((t, []), None), NotImplemented)
self.assertEqual(dispatcher.Dispatch(('foo', [rt]), None), NotImplemented)
self.assertEqual(dispatcher.Dispatch(('foo', 'bar'), None), NotImplemented)
self.assertEqual(
    dispatcher.Dispatch(('foo', 'bar', 'baz'), None), NotImplemented)
