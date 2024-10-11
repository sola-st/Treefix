# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
nonlocal restore_count
if op_type == b"RestoreV2":
    restore_count += 1
