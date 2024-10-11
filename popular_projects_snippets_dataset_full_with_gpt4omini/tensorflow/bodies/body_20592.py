# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/topology_test.py
"""Tests if the class is able to generate serialized strings."""
original_topology = topology.Topology(
    mesh_shape=[1, 1, 1, 2],
    device_coordinates=[[[0, 0, 0, 0], [0, 0, 0, 1]]],
)
serialized_str = original_topology.serialized()
new_topology = topology.Topology(serialized=serialized_str)

# Make sure the topology recovered from serialized str is same as the
# original topology.
self.assertAllEqual(
    original_topology.mesh_shape, new_topology.mesh_shape)
self.assertAllEqual(
    original_topology.device_coordinates, new_topology.device_coordinates)
