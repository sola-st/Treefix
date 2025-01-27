# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_utils_test.py
cls._sess = session.Session()
with cls._sess:
    cls._a_init_val = np.array([[5.0, 3.0], [-1.0, 0.0]])
    cls._b_init_val = np.array([[2.0], [-1.0]])
    cls._c_val = np.array([[-4.0], [np.nan]])

    cls._a_init = constant_op.constant(
        cls._a_init_val, shape=[2, 2], name="a1_init")
    cls._b_init = constant_op.constant(
        cls._b_init_val, shape=[2, 1], name="b_init")

    cls._a = variables.VariableV1(cls._a_init, name="a1")
    cls._b = variables.VariableV1(cls._b_init, name="b")
    cls._c = constant_op.constant(cls._c_val, shape=[2, 1], name="c")

    # Matrix product of a and b.
    cls._p = math_ops.matmul(cls._a, cls._b, name="p1")

    # Sum of two vectors.
    cls._s = math_ops.add(cls._p, cls._c, name="s")

cls._graph = cls._sess.graph

# These are all the expected nodes in the graph:
#   - Two variables (a, b), each with four nodes (Variable, init, Assign,
#     read).
#   - One constant (c).
#   - One add operation and one matmul operation.
#   - One wildcard node name ("*") that covers nodes created internally
#     by TensorFlow itself (e.g., Grappler).
cls._expected_num_nodes = 4 * 2 + 1 + 1 + 1 + 1
