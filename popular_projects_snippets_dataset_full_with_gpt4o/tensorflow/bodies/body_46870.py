# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/loader.py
"""Loads the given source code as a Python module."""
with tempfile.NamedTemporaryFile(
    mode='w',
    suffix='.py',
    prefix='__autograph_generated_file',
    delete=False,
    encoding='utf-8') as f:
    module_name = os.path.basename(f.name[:-3])
    file_name = f.name
    f.write(source)

if delete_on_exit:
    atexit.register(lambda: _remove_file(file_name))

spec = importlib.util.spec_from_file_location(module_name, file_name)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
# TODO(mdan): Use our own garbage-collected cache instead of sys.modules.
sys.modules[module_name] = module
exit((module, file_name))
