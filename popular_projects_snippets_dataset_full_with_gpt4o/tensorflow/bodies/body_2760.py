# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
x = array_ops.placeholder(dtypes.int32, name='x_hold')
y = variables.VariableV1(constant_op.constant([0]), name='y_saved')
math_ops.add(x, y, name='x_y_sum')

init_op = variables.global_variables_initializer()
saver = saver_lib.Saver(write_version=saver_pb2.SaverDef.V1)
with session.Session() as sess:
    sess.run(init_op)
    sess.run(y.assign(y + 42))
    # Without the checkpoint, the variable won't be set to 42.
    ckpt = os.path.join(out_dir, 'test_graph_tfadd_with_ckpt.ckpt')
    saver.save(sess, ckpt)
