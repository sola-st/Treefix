# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/generate_examples_lib.py

def mkdir_if_not_exist(x):
    if not os.path.isdir(x):
        os.mkdir(x)
        if not os.path.isdir(x):
            raise RuntimeError("Failed to create dir %r" % x)

opstest_path = os.path.join(options.output_path)
mkdir_if_not_exist(opstest_path)
