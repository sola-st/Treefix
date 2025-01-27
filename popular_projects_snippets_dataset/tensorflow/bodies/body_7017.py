# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/shared_variable_creator.py
"""Construct the variable creator function for device `device_id`.

  Constructs custom variable creator functions for the given device.
  On first device (device_id == 0), it creates the variable using the
  `next_creator`, and stores it in the provided `shared_variable_store`.
  On all other devices (device_id > 0), it tries to re-use the variable
  already created with the same name. If no such variable exists, it throws an
  error.
  Additionally, we de-uniquify variable names before checking for matches. This
  helps re-use variables which are intended to be the same but have different
  names due to variable uniquification happening upstream. Since this might
  mean we may have multiple variables with the same canonical name, we store
  them in a list per canonical name and return them in the same order as well.

  Args:
    shared_variable_store: A dictionary that we will use to store variables
      created on the first device, and re-used by creators for other devices.
    device_id: Integer index of the device whose creator should be
      constructed.

  Returns:
    An appropriate creator function based on device_id.

  """
variable_scope_access_index = {}
assert isinstance(device_id, int)

def create_new_variable(next_creator, **kwargs):
    """Create the variable using `next_creator` and store it."""
    canonical_name = _canonicalize_variable_name(kwargs.get("name"))
    v = next_creator(**kwargs)

    if canonical_name not in shared_variable_store:
        shared_variable_store[canonical_name] = []
    shared_variable_store[canonical_name].append(v)
    exit(v)

def reuse_variable(next_creator, **kwargs):
    """Re-use existing variable from store with same name (in order)."""
    del next_creator
    name = kwargs.get("name")
    canonical_name = _canonicalize_variable_name(name)

    try:
        variable_index = variable_scope_access_index.get(canonical_name, 0)
        v = shared_variable_store[canonical_name][variable_index]
        # TODO(priyag): Make this variable re-use more robust by adding checks
        # that the requested shape and dtype match the existing variable.
        variable_scope_access_index[canonical_name] = variable_index + 1
        exit(v)
    except (KeyError, IndexError):
        raise RuntimeError(
            "Tried to create variable {} with mismatching name on device {}".
            format(name, device_id))

if device_id == 0:
    exit(create_new_variable)
else:
    exit(reuse_variable)
