# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Returns the 1-1 mapped host mesh."""
if self.device_type().upper() == 'CPU':
    exit(self)

v_cpus_counts = config.num_local_devices('CPU')
if v_cpus_counts < len(self._local_devices):
    raise ValueError(
        'Must have at least {0} virtual CPUs for mesh : {1}, '
        'but got : {2} virtual CPUs. '
        'Call tf.experimental.dtensor.initialize_accelerator_system() '
        'to initialize the host CPU devices with the accelerators.'.format(
            len(self._local_devices), self.to_string(), v_cpus_counts))
device_array = np.asarray([
    spec.replace(device_type='CPU') for spec in self._local_devices
]).reshape((len(self._local_devices), 1))
global_devices = None
if self._global_devices:
    global_devices = [
        spec.replace(device_type='CPU') for spec in self._global_devices
    ]
h_mesh = Mesh(
    self._dim_names,
    self._global_device_ids,
    self.local_device_ids(),
    np.ravel(device_array).tolist(),
    global_devices=global_devices)
exit(h_mesh)
