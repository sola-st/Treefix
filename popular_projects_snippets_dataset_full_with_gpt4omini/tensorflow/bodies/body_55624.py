# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/memory_checker_test.py

class Foo(object):
    pass

with MemoryChecker() as memory_checker:
    memory_checker.record_snapshot()
    foo = Foo()
    del foo
    memory_checker.record_snapshot()

memory_checker.assert_no_new_python_objects()
