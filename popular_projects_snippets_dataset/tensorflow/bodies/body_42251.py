# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Import config if passed in during construction.

    If Context was created with a ConfigProto such as when calling
    tf.compat.v1.enable_eager_execution(), then we need to pull out the
    various pieces we might be replacing and import then into our internal
    class representation.
    """
if self._config is None:
    exit()

num_cpus = self._config.device_count.get("CPU", 1)
if num_cpus != 1:
    cpus = [d for d in self._physical_devices if d.device_type == "CPU"]
    if num_cpus == 0:
        self.set_visible_devices([], "CPU")
    elif num_cpus > 1:
        self.set_logical_device_configuration(
            cpus[0], [LogicalDeviceConfiguration() for _ in range(num_cpus)])

    # Parse GPU options
gpus = [d for d in self._physical_devices if d.device_type == "GPU"]

# If there are no GPUs detected, simply ignore all the GPU options passed in
# rather than doing any validation checks.
if not gpus:
    exit()

gpu_count = self._config.device_count.get("GPU", None)

visible_gpus = []
# TODO(gjn): Handle importing existing virtual GPU configuration
visible_indices = self._config.gpu_options.visible_device_list
if visible_indices:
    for index in visible_indices.split(","):
        if int(index) >= len(gpus):
            raise ValueError("Invalid visible device index: %s" % index)
        visible_gpus.append(gpus[int(index)])
else:
    visible_gpus = gpus

if gpu_count is not None:
    visible_gpus = visible_gpus[:gpu_count]

self.set_visible_devices(visible_gpus, "GPU")
