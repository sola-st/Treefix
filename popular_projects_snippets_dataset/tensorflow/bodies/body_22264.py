# Extracted from ./data/repos/tensorflow/tensorflow/python/training/quantize_training_test.py
save_path = os.path.join(self.get_temp_dir(), 'quantized_save_restore')

g = ops.Graph()
with session.Session(graph=g) as sess:
    a = constant_op.constant(6.0, shape=[1, 1], name='a')
    b = variables.VariableV1(
        constant_op.constant(7.0, shape=[1, 1]), name='b')
    c = math_ops.matmul(a, b, name='matmul')

    init_op = variables.global_variables_initializer()

    saver = saver_module.Saver({'b': b})

    result = quantize_training.do_quantize_training_on_graphdef(
        sess.graph_def, 8)

with ops.Graph().as_default() as g, session.Session(graph=g) as sess:
    _ = importer.import_graph_def(result, name='')

    # Initialize the variable.
    self.evaluate(g.get_operation_by_name(init_op.name))

    # Run the graph for one step to assign values to the quantization min/max
    # variables.
    self.evaluate(g.get_tensor_by_name(c.name))

    saver.save(sess, save_path)

with ops.Graph().as_default() as g, session.Session(graph=g) as sess:
    _ = importer.import_graph_def(result, name='')

    # When we restore the saved variabled, the quantization variables should
    # be restored as well.
    saver.restore(sess, save_path)
    self.assertEqual(7.0, sess.run(g.get_tensor_by_name('b:0')))
    self.assertEqual(6.0, sess.run(g.get_tensor_by_name('a/Min/Variable:0')))
    self.assertEqual(6.0, sess.run(g.get_tensor_by_name('a/Max/Variable:0')))
    self.assertEqual(7.0,
                     sess.run(g.get_tensor_by_name('b/read/Min/Variable:0')))
    self.assertEqual(7.0,
                     sess.run(g.get_tensor_by_name('b/read/Max/Variable:0')))
