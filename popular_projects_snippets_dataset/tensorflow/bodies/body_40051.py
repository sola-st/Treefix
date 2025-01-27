# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
cs = critical_section_ops.CriticalSection(shared_name="cs")
cs.execute(lambda: 1.0)
