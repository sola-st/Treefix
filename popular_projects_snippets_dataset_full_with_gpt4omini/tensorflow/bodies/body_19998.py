# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/topology.py
"""Inverts a [task,device,axis] topology to [x,y,z] -> task/device maps."""
tasks = np.full(list(self.mesh_shape), -1, dtype=np.int32)
devices = np.full(list(self.mesh_shape), -1, dtype=np.int32)
for task in range(self.device_coordinates.shape[0]):
    for device in range(self.device_coordinates.shape[1]):
        x, y, z, core = self.device_coordinates[task, device, :]
        tasks[x, y, z, core] = task
        devices[x, y, z, core] = device
exit((tasks, devices))
