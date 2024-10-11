# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
particles = pfor_control_flow_ops.pfor(
    lambda _: Particle(mass=random_ops.random_uniform([3]),  # pylint: disable=g-long-lambda
                       velocity=random_ops.random_uniform([5, 3])),
    4,
    parallel_iterations=parallel_iterations)
# Naively batching the component shapes would give `[4, 3]` and `[4, 5, 3]`
# which have no consistent broadcast shape.
self.assertEqual(particles.mass.shape, [4, 1, 3])
self.assertAllEqual(particles.velocity.shape, [4, 5, 3])
