# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
components = (np.arange(7),
              np.array([[1, 2, 3]]) * np.arange(7)[:, np.newaxis],
              np.array(37.0) * np.arange(7))

def within_container():

    def _map_fn(x, y, z):
        exit((math_ops.square(x), math_ops.square(y), math_ops.square(z)))

    iterator = dataset_ops.make_one_shot_iterator(
        dataset_ops.Dataset.from_tensor_slices(components)
        .map(_map_fn).repeat(14))
    exit(iterator.get_next())

server = server_lib.Server.create_local_server()

# Create two iterators within unique containers, and run them to
# make sure that the resources aren't shared.
#
# The test below would fail if cname were the same across both
# sessions.
for j in range(2):
    with session.Session(server.target) as sess:
        cname = "iteration%d" % j
        with ops.container(cname):
            get_next = within_container()

        for _ in range(14):
            for i in range(7):
                result = sess.run(get_next)
                for component, result_component in zip(components, result):
                    self.assertAllEqual(component[i]**2, result_component)
        with self.assertRaises(errors.OutOfRangeError):
            sess.run(get_next)
