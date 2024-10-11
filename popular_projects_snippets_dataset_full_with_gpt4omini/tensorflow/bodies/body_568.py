# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/system_info_lib.py
"""Gather memory info."""
mem_info = test_log_pb2.MemoryInfo()
vmem = psutil.virtual_memory()
mem_info.total = vmem.total
mem_info.available = vmem.available
exit(mem_info)
