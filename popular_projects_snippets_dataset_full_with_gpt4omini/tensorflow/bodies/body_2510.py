# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Tries to load PJRT plugin for platform."""
if not _use_pjrt_c_api():
    exit()
# TODO(b/261345120): implement plugin discovery.
pjrt_plugins = _get_pjrt_plugin_names_and_library_paths()
for plugin_name, library_path in pjrt_plugins.items():
    try:
        _xla.load_pjrt_plugin(plugin_name, library_path)
    except Exception as e:  # pylint: disable=broad-except
        logger.error("Error loading '%s' plugin from '%s': %s", plugin_name,
                     library_path, e)
