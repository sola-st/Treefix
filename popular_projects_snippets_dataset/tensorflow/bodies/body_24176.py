# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/disk_usage_test.py
# For efficient testing, set the disk usage bytes limit to a small
# number (10).
os.environ["TFDBG_DISK_BYTES_LIMIT"] = "10"
