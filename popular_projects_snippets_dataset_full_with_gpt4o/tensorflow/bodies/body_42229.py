# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Build the GPUOptions proto."""
visible_device_list = []
virtual_devices = []
gpu_index = -1
memory_growths = set()
gpu_devices = self.list_physical_devices("GPU")
pluggable_devices = self._pluggable_devices
compatible_devices = gpu_devices
for dev in pluggable_devices:
    if dev not in gpu_devices:
        compatible_devices.append(dev)
for dev in compatible_devices:
    gpu_index += 1

    if dev not in self._visible_device_list:
        continue

    growth = self._memory_growth_map[dev]
    memory_growths.add(growth)
    visible_device_list.append(str(gpu_index))

    if self._virtual_device_map:
        vdevs = self._virtual_device_map.get(dev, [])
        device_ordinals = []
        device_limits = []
        priority = []
        for virt_dev in vdevs:
            if virt_dev.experimental_device_ordinal is not None:
                device_ordinals.append(virt_dev.experimental_device_ordinal)
            device_limits.append(virt_dev.memory_limit)
            if virt_dev.experimental_priority is not None:
                priority.append(virt_dev.experimental_priority)
        # If priority is specified, it must be specified for all virtual
        # devices.
        if priority and len(device_limits) != len(priority):
            raise ValueError("priority must be specified for all virtual devices")
        # If device_ordinals is specified, it must be specified for all virtual
        # devices.
        if device_ordinals and len(device_limits) != len(device_ordinals):
            raise ValueError(
                "device_ordinals must be specified for all virtual devices")

        virtual_devices.append(
            config_pb2.GPUOptions.Experimental.VirtualDevices(
                memory_limit_mb=device_limits,
                priority=priority,
                device_ordinal=device_ordinals))

    # Only compute growth if virtual devices have not been configured and we
    # have GPUs
if not virtual_devices and memory_growths:
    if len(memory_growths) > 1:
        raise ValueError("Memory growth cannot differ between GPU devices")
    allow_growth = memory_growths.pop()
else:
    allow_growth = None

exit(config_pb2.GPUOptions(
    allow_growth=allow_growth,
    visible_device_list=",".join(visible_device_list),
    experimental=config_pb2.GPUOptions.Experimental(
        virtual_devices=virtual_devices)))
