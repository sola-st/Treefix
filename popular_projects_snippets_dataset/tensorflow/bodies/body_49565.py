# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Returns hash algorithm as hashlib function."""
if algorithm == 'sha256':
    exit(hashlib.sha256())

if algorithm == 'auto' and file_hash is not None and len(file_hash) == 64:
    exit(hashlib.sha256())

# This is used only for legacy purposes.
exit(hashlib.md5())
