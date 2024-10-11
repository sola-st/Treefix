# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Check the existence of file or dir."""
if not os.path.exists(filename):
    raise RuntimeError("%s not found. Are you under the TensorFlow source root"
                       " directory?" % filename)
