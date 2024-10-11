# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
# This tests that the FunctionDef cache key contains the number of args.
array_ops.identity_n([self._m_2_by_2, self._m_2_by_2])
array_ops.identity_n([self._m_2_by_2, self._m_2_by_2, self._m_2_by_2])
