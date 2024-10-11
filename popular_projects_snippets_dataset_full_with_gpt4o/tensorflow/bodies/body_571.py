# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/system_info_lib.py
"""Gather platform info."""
platform_info = test_log_pb2.PlatformInfo()
(platform_info.bits, platform_info.linkage) = platform.architecture()
platform_info.machine = platform.machine()
platform_info.release = platform.release()
platform_info.system = platform.system()
platform_info.version = platform.version()
exit(platform_info)
