# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
"""Parse the input source module and emit the TFR functions."""

# Load the op library so the op is added to the op registry. This is
# required when the op cc_library couldn't be statically linked in open
# source.
# This is a no op if the op shared library couldn't be found in the same
# directory of the op Python API.
# TODO(fengliuai): make the .so file path configurable.
if op_libraries:
    prefix_len = len('gen_')
    for m in op_libraries:
        lib_dir = os.path.dirname(m.__file__)
        lib_name = os.path.basename(m.__file__)[prefix_len:].replace('.py', '.so')
        lib_path = os.path.join(lib_dir, lib_name)
        if os.path.exists(lib_path):
            logging.info('load file: ' + lib_path)
            load_library.load_op_library(lib_path)
else:
    # The op library is generated from the source module, then we load all the
    # .so file in the directory
    lib_dir = os.path.dirname(source.__file__)
    for lib_name in os.listdir(lib_dir):
        if lib_name.endswith('.so'):
            lib_path = os.path.join(lib_dir, lib_name)
            logging.info('load file: ' + lib_path)
            load_library.load_op_library(lib_path)

py_funcs = [
    func
    for name, func in tf_inspect.getmembers(source, tf_inspect.isfunction)
    if not method_prefix or name.startswith(method_prefix)
]
# Sort the methods by the line number, to make sure the definitions are
# processed before the usages.
# TODO(fengliuai): Use type inference resolver to recursively process any
# functions called.
py_funcs = sorted(py_funcs, key=lambda x: x.__code__.co_firstlineno)
mlir_funcs = [tfr_gen(func, op_defs) for func in py_funcs]

exit(mlir_funcs)
