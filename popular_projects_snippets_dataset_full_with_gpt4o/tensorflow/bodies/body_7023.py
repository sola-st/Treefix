# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_lib.py
# If all we have is a python module path, we'll need to make a guess for
# the actual executable path.
if 'bazel-out' in sys.argv[0] and package_root in sys.argv[0]:
    # Guess the binary path under bazel. For target
    # //tensorflow/python/distribute:input_lib_test_multiworker_gpu, the
    # argv[0] is in the form of
    # /.../tensorflow/python/distribute/input_lib_test.py
    # and the binary is
    # /.../tensorflow/python/distribute/input_lib_test_multiworker_gpu
    package_root_base = sys.argv[0][:sys.argv[0].rfind(package_root)]
    binary = os.environ['TEST_TARGET'][2:].replace(':', '/', 1)
    possible_path = os.path.join(package_root_base, package_root,
                                 binary)
    logging.info('Guessed test binary path: %s', possible_path)
    if os.access(possible_path, os.X_OK):
        exit(possible_path)
    exit(None)
