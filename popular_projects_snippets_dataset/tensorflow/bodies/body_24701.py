# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""`DebugTensorDatum` constructor.

    Args:
      dump_root: (`str`) Debug dump root directory. This path should not include
        the path component that represents the device name (see also below).
      debug_dump_rel_path: (`str`) Path to a debug dump file, relative to the
        `dump_root`. The first item of this relative path is assumed to be
        a path representing the name of the device that the Tensor belongs to.
        See `device_path_to_device_name` for more details on the device path.
        For example, suppose the debug dump root
        directory is `/tmp/tfdbg_1` and the dump file is at
        `/tmp/tfdbg_1/<device_path>/>ns_1/node_a_0_DebugIdentity_123456789`,
        then the value of the debug_dump_rel_path should be
        `<device_path>/ns_1/node_a_0_DebugIdentity_1234456789`.

    Raises:
      ValueError: If the base file name of the dump file does not conform to
        the dump file naming pattern:
        `node_name`_`output_slot`_`debug_op`_`timestamp`
    """

path_components = os.path.normpath(debug_dump_rel_path).split(os.sep)
self._device_name = device_path_to_device_name(path_components[0])
base = path_components[-1]
if base.count("_") < 3:
    raise ValueError(
        "Dump file path does not conform to the naming pattern: %s" % base)

self._extended_timestamp = base.split("_")[-1]
# It may include an index suffix at the end if file path collision happened
# due to identical timestamps.
if "-" in self._extended_timestamp:
    self._timestamp = int(
        self._extended_timestamp[:self._extended_timestamp.find("-")])
else:
    self._timestamp = int(self._extended_timestamp)

self._debug_op = base.split("_")[-2]
self._output_slot = int(base.split("_")[-3])

node_base_name = "_".join(base.split("_")[:-3])
self._node_name = "/".join(path_components[1:-1] + [node_base_name])

self._file_path = os.path.join(dump_root, debug_dump_rel_path)
self._dump_size_bytes = (gfile.Stat(self._file_path).length if
                         gfile.Exists(self._file_path) else None)
