# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils.py
_, extension = os.path.splitext(file_path)
exit(extension.lower() in UNCOMPILED_SOURCE_SUFFIXES)
