# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_dispatcher_test.py
dispatcher = dispatch.PythonAPIDispatcher('tf.foo', ['x', 'y', 'name'],
                                          (None,))

rt_checker = dispatch.MakeInstanceChecker(ragged_tensor.RaggedTensor)
rt_x_checker = dispatch.PySignatureChecker([(0, rt_checker)])
rt_y_checker = dispatch.PySignatureChecker([(1, rt_checker)])

f1 = lambda x, y, name=None: 'f1'
f2 = lambda x, y, name=None: 'f2'

rt = ragged_factory_ops.constant([[1, 2], [3]])

dispatcher.Register(rt_x_checker, f1)
dispatcher.Register(rt_y_checker, f2)

self.assertEqual(dispatcher.Dispatch((rt, 5), None), 'f1')
self.assertEqual(dispatcher.Dispatch(('foo', rt), None), 'f2')
self.assertEqual(dispatcher.Dispatch(('foo',), {'y': rt}), 'f2')
self.assertEqual(dispatcher.Dispatch(('foo', 'bar'), None), NotImplemented)
with self.assertRaisesRegex(
    ValueError, 'Multiple dispatch targets .*'
    r'match the arguments to tf\.foo'):
    dispatcher.Dispatch((rt, rt), None)
