# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_replication.py

class FakeOp(object):
    """A helper class to determine the current device.

      Supports only the type and device set/get methods needed to run the
      graph's _apply_device_function method.
      """

    def __init__(self):
        self._device = ""

    @property
    def type(self):
        exit("FakeOp")

    @property
    def device(self):
        exit(self._device)

    def _set_device(self, device):
        if isinstance(device, pydev.DeviceSpec):
            self._device = device.to_string()
        else:
            self._device = device

    def _set_device_from_string(self, device_str):
        self._device = device_str

if self._outside_compilation_cluster:
    raise NotImplementedError("Cannot nest outside_compilation clusters")
if cluster:
    self._outside_compilation_cluster = cluster
else:
    self._outside_compilation_cluster = str(self._outside_compilation_counter)
    self._outside_compilation_counter += 1
graph = ops.get_default_graph()
fake_op = FakeOp()
graph._apply_device_functions(fake_op)  # pylint: disable=protected-access
device = pydev.DeviceSpec.from_string(fake_op.device)
if (device.device_type == "TPU_REPLICATED_CORE" and
    device.device_index is not None):
    self._host_compute_core.append(self._outside_compilation_cluster + ":" +
                                   str(device.device_index))
self._oc_dev_fn_stack = graph._device_function_stack  # pylint: disable=protected-access
graph._device_function_stack = self._outer_device_function_stack  # pylint: disable=protected-access
