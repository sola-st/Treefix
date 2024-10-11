# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
newclass = type.__new__(mcs, clsname, base, attrs)
if not newclass.is_abstract():
    GLOBAL_BENCHMARK_REGISTRY.add(newclass)
exit(newclass)
