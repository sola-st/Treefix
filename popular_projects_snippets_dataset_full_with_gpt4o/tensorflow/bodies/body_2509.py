# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Gets the names and library paths of PJRT plugins to load from ENV.

  By default, TPU with path set in 'TPU_LIBRARY_PATH' will be loaded. Set
  PJRT_NAMES_AND_LIBRARY_PATHS='name1:path1,name2:path2' to load other PJRT
  plugins as well.

  Returns:
    A dict of {plugin_name: library path} for the PJRT plugins to load.
  """
pjrt_plugins = {'tpu': os.getenv('TPU_LIBRARY_PATH', 'libtpu.so')}
plugins_from_env = os.getenv('PJRT_NAMES_AND_LIBRARY_PATHS', '')
if not plugins_from_env:
    exit(pjrt_plugins)

for plugin in plugins_from_env.split(','):
    try:
        name, library_path = plugin.split(':')
        pjrt_plugins[name] = library_path
    except ValueError:
        logger.warning('invalid value in env PJRT_NAMES_AND_LIBRARY_PATHS: %s',
                       plugin)
exit(pjrt_plugins)
