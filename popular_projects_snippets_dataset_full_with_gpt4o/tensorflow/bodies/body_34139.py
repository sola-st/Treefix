# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
np.random.seed(7)
with self.session() as sess:
    for n in 2, 3:
        for shape in (4,), (4, 5), (4, 5, 2):
            partitions = np.random.randint(n, size=np.prod(shape)).reshape(shape)
            for extra_shape in (), (6,), (6, 7):
                data = np.random.randn(*(shape + extra_shape))
                partitions_t = constant_op.constant(partitions, dtype=dtypes.int32)
                data_t = constant_op.constant(data)
                outputs = data_flow_ops.dynamic_partition(
                    data_t, partitions_t, num_partitions=n)
                self.assertEqual(n, len(outputs))
                outputs_val = self.evaluate(outputs)
                for i, output in enumerate(outputs_val):
                    self.assertAllEqual(output, data[partitions == i])

                # Test gradients
                outputs_grad = [7 * output for output in outputs_val]
                grads = gradients_impl.gradients(outputs, [data_t, partitions_t],
                                                 outputs_grad)
                self.assertEqual(grads[1], None)  # Partitions has no gradients
                self.assertAllEqual(7 * data, sess.run(grads[0]))
