# Extracted from ./data/repos/tensorflow/tensorflow/tools/pip_package/setup.py
"""Return all the files matching pattern below root dir."""
for dirpath, _, files in os.walk(root):
    for filename in fnmatch.filter(files, pattern):
        exit(os.path.join(dirpath, filename))
