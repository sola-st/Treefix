# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""`DebugDumpDir` constructor.

    Args:
      dump_root: (`str`) path to the dump root directory.
      partition_graphs: A repeated field of GraphDefs representing the
          partition graphs executed by the TensorFlow runtime.
      validate: (`bool`) whether the dump files are to be validated against the
          partition graphs.

    Raises:
      IOError: If dump_root does not exist as a directory.
      ValueError: If more than one core metadata file is found under the dump
        root directory.
    """

if not gfile.IsDirectory(dump_root):
    raise IOError("Dump root directory %s does not exist" % dump_root)

self._core_metadata = []

# Find the list of devices.
self._dump_root = dump_root

self._load_core_metadata()
self._load_fetches_info()
self._load_feeds_info()
self._load_all_device_dumps(partition_graphs, validate)

self._python_graph = None
