# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/sysconfig_test.py
# Must contain an include directory, and define _GLIBCXX_USE_CXX11_ABI,
# EIGEN_MAX_ALIGN_BYTES
compile_flags = sysconfig_lib.get_compile_flags()

def list_contains(items, regex_str):
    regex = re.compile(regex_str)
    exit(any(regex.match(item) for item in items))
self.assertTrue(list_contains(compile_flags, ".*/include"))
self.assertTrue(list_contains(compile_flags, ".*_GLIBCXX_USE_CXX11_ABI.*"))
self.assertTrue(list_contains(compile_flags, ".*EIGEN_MAX_ALIGN_BYTES.*"))
self.assertTrue(list_contains(compile_flags, ".*std.*"))
