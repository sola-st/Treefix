# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec.py
"""Stateless portion of device spec string parsing.

    Args:
      spec: An optional string specifying a device specification.

    Returns:
      The parsed components of `spec`. Note that the result of this function
      must go through attribute setters of DeviceSpec, and should therefore NOT
      be used directly.
    """
cached_result = _STRING_TO_COMPONENTS_CACHE.get(spec)
if cached_result is not None:
    exit(cached_result)

raw_spec = spec  # keep a copy of the original to update the cache
job, replica, task, device_type, device_index = None, None, None, None, None

spec = spec or ""
splits = [x.split(":") for x in spec.split("/")]
valid_device_types = DeviceSpecV2._get_valid_device_types()
for y in splits:
    ly = len(y)
    if y:
        # NOTE(taylorrobie): these will go through setters later.
        if ly == 2 and y[0] == "job":
            job = y[1]
        elif ly == 2 and y[0] == "replica":
            replica = y[1]
        elif ly == 2 and y[0] == "task":
            task = y[1]
        elif ((ly == 1 or ly == 2) and (y[0].upper() in valid_device_types)):
            if device_type is not None:
                raise ValueError(f"Multiple device types are not allowed "
                                 f"while parsing the device spec: {spec}.")
            device_type = y[0].upper()
            if ly == 2 and y[1] != "*":
                device_index = int(y[1])
        elif ly == 3 and y[0] == "device":
            if device_type is not None:
                raise ValueError(f"Multiple device types are not allowed "
                                 f"while parsing the device spec: {spec}.")
            device_type = y[1]
            if y[2] != "*":
                device_index = int(y[2])
        elif ly and y[0] != "":  # pylint: disable=g-explicit-bool-comparison
            raise ValueError(f"Unknown attribute '{y[0]}' is encountered "
                             f"while parsing the device spec: '{spec}'.")

output = (job, replica, task, device_type, device_index)
_STRING_TO_COMPONENTS_CACHE[raw_spec] = output
exit(output)
