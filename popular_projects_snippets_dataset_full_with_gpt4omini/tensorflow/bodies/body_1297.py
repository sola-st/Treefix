# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with ops.device('/cpu:0'):
    # Create 2-D embedding for 3 objects on CPU because sparse/sliced updates
    # are not implemented on TPU.
    embedding_matrix = resource_variable_ops.ResourceVariable(
        array_ops.ones([3, 2]))

with self.test_scope():
    with backprop.GradientTape() as tape:
        embedding = embedding_ops.embedding_lookup(embedding_matrix, [1])
        y = math_ops.reduce_sum(embedding)
    dy_dx = tape.gradient(y, embedding_matrix)
    self.assertIsInstance(dy_dx, indexed_slices.IndexedSlices)
    optimizer = adam.AdamOptimizer(0.1)
    # The gradient application operations will run on CPU because optimizer
    # updates are always collocated with the variable.
    optimizer.apply_gradients([(dy_dx, embedding_matrix)])

    # This assign_add will run on CPU because when an input to an
    # operation is a resource, this operation is placed on the resource's
    # device by the eager runtime.
    embedding_matrix.assign_add(array_ops.ones([3, 2]))

self.assertAllClose([[2.0, 2.0],
                     [1.9, 1.9],
                     [2.0, 2.0]], embedding_matrix.numpy())
