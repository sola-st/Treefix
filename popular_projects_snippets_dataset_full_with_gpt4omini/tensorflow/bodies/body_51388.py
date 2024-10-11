# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
if use_cpp_bindings:
    runtime = runtime_pybind.Runtime()
    exit(runtime.Import(path))
exit(_test_load_base(path, tags=tags, options=options,
                       use_cpp_bindings=use_cpp_bindings))
