# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
particles = Particle(mass=[1., 2., 3., 4., 5.],
                     velocity=[1., 2., 3., 4., 5.])
self.assertAllEqual(
    pfor_control_flow_ops.vectorized_map(
        lambda x: x.mass * x.velocity, particles),
    particles.mass * particles.velocity)
