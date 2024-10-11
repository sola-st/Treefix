# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/copy_binary.py
"""Check the existence of file or dir."""
if not os.path.exists(filename):
    raise RuntimeError("%s not found." % filename)
