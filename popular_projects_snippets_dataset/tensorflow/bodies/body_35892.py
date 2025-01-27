# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session():
    rnd = variables.Variable(random_ops.random_uniform([10, 43]))
    with self.assertRaises(ValueError):
        partitioned_variables.create_partitioned_variables(
            [10], [1, 1], rnd.initialized_value())
    with self.assertRaises(ValueError):
        partitioned_variables.create_partitioned_variables(
            [10, 20], [1], rnd.initialized_value())
    with self.assertRaises(ValueError):
        partitioned_variables.create_partitioned_variables(
            [10, 43], [1], rnd.initialized_value())
    with self.assertRaises(ValueError):
        partitioned_variables.create_partitioned_variables(
            [10, 43], [1, 2, 3], rnd.initialized_value())
    with self.assertRaises(ValueError):
        partitioned_variables.create_partitioned_variables(
            [10, 43], [11, 1], rnd.initialized_value())
    with self.assertRaises(ValueError):
        partitioned_variables.create_partitioned_variables(
            [10, 43], [20, 1], rnd.initialized_value())
    with self.assertRaises(ValueError):
        partitioned_variables.create_partitioned_variables(
            [10, 43], [1, 50], rnd.initialized_value())
