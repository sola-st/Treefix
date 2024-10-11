# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
repeats = [[1, 2], [3, 4], [5, 0], [1, 7]]
components = np.array(repeats, dtype=np.int64)
iterator = (
    dataset_ops.make_initializable_iterator(
        dataset_ops.Dataset.from_tensor_slices(components).flat_map(
            lambda x: dataset_ops.Dataset.from_tensor_slices(x).flat_map(
                lambda y: dataset_ops.Dataset.from_tensors(y).repeat(y))),
        shared_name="shared_flat_map_iterator"))
init_op = iterator.initializer
get_next = iterator.get_next()

# Create two concurrent sessions that share the same iterator
# resource on the same server, and verify that a random
# interleaving of `Session.run(get_next)` calls on the two
# sessions yields the expected result.
server = server_lib.Server.create_local_server()
with session.Session(server.target) as sess1:
    with session.Session(server.target) as sess2:
        for _ in range(3):
            sess = random.choice([sess1, sess2])
            sess.run(init_op)
            for row in repeats:
                for i in row:
                    for _ in range(i):
                        sess = random.choice([sess1, sess2])
                        self.assertEqual(i, sess.run(get_next))

        with self.assertRaises(errors.OutOfRangeError):
            sess = random.choice([sess1, sess2])
            sess.run(get_next)
