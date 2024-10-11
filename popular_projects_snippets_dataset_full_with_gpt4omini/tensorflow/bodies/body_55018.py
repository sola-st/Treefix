# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
dispatcher = dispatch.PythonAPIDispatcher('tf.foo', ['x', 'y', 'name'],
                                          (None,))

rt_checker = dispatch.MakeInstanceChecker(ragged_tensor.RaggedTensor)
f1 = lambda x, y, name=None: 'f1'
dispatcher.Register(dispatch.PySignatureChecker([(0, rt_checker)]), f1)

rt = ragged_factory_ops.constant([[1, 2], [3]])
self.assertEqual(dispatcher.Dispatch((rt, 5), None), 'f1')
self.assertEqual(dispatcher.Dispatch((rt, 5, 'my_name'), None), 'f1')
self.assertEqual(dispatcher.Dispatch((), {'x': rt, 'y': 5}), 'f1')
self.assertEqual(
    dispatcher.Dispatch((), {
        'x': rt,
        'y': 5,
        'name': 'x'
    }), 'f1')
self.assertEqual(dispatcher.Dispatch(('foo', rt), None), NotImplemented)
self.assertEqual(dispatcher.Dispatch(('foo', 'bar'), None), NotImplemented)
self.assertEqual(
    dispatcher.Dispatch(('foo', 'bar', 'baz'), None), NotImplemented)
