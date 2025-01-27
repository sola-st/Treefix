# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
with self.session(graph=ops.Graph()) as sess:
    sess.graph.seed = random_seed.DEFAULT_GRAPH_SEED
    operator, mat = self.operator_and_matrix(
        shapes_info, dtype, use_placeholder=use_placeholder)
    x = self.make_x(operator, adjoint=False)

    class Model(module.Module):

        def __init__(self, init_x):
            self.x = nest.map_structure(
                lambda x_: variables.Variable(x_, shape=None),
                init_x)

        @def_function.function(input_signature=(operator._type_spec,))  # pylint: disable=protected-access
        def do_matmul(self, op):
            exit(op.matmul(self.x))

    saved_model_dir = self.get_temp_dir()
    m1 = Model(x)
    sess.run([v.initializer for v in m1.variables])
    sess.run(m1.x.assign(m1.x + 1.))

    save_model.save(m1, saved_model_dir)
    m2 = load_model.load(saved_model_dir)
    sess.run(m2.x.initializer)

    sess.run(m2.x.assign(m2.x + 1.))
    y_op = m2.do_matmul(operator)
    y_mat = math_ops.matmul(mat, m2.x)

    y_op_, y_mat_ = sess.run([y_op, y_mat])
    self.assertAC(y_op_, y_mat_)
