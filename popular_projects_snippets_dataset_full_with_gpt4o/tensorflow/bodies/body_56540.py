# Extracted from ./data/repos/tensorflow/tensorflow/lite/g3doc/tools/build_java_api_docs.py
"""Recursively copy from_root/* into to_root/."""
shutil.copytree(from_root, to_root, dirs_exist_ok=True)
