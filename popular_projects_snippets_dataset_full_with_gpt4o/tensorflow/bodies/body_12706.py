# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/critical_section_ops.py
"""Initialize the CriticalSection from constructor arguments."""
with ops.name_scope(name, "CriticalSection", []) as name:
    with ops.init_scope():
        # pylint: disable=protected-access
        container = ops.get_default_graph()._container
        # pylint: enable=protected-access
        if shared_name is None:
            shared_name = name
        if container is None:
            container = ""
        self._handle = gen_resource_variable_ops.mutex_v2(
            shared_name=shared_name, container=container, name=name)
        # Get a uniquely identifying signature for the handle.
        self._signature = (
            container,
            # If shared_name is empty, a unique CriticalSection is created.
            shared_name or id(self._handle),
            _get_device_or_colocation(self._handle))

if not context.executing_eagerly():
    ops.add_to_collections(CRITICAL_SECTIONS, self)
