# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
num_particles = 10
velocities = random_ops.random_uniform([num_particles])
particles = pfor_control_flow_ops.pfor(
    # Build a batch of particles all with the same mass.
    lambda i: Particle(mass=4., velocity=array_ops.gather(velocities, i)),
    num_particles,
    parallel_iterations=parallel_iterations)
particles_mass, particles_velocity, velocities = self.evaluate(
    (particles.mass, particles.velocity, velocities))
self.assertAllEqual(particles_mass, 4. * np.ones([num_particles]))
self.assertAllEqual(particles_velocity, velocities)
