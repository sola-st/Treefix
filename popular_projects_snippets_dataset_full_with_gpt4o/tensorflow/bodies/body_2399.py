# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tf2xla/light_outside_compilation_test.py
"""Assert that FileCheck runs successfully."""
if not fw.check(actual, expected):
    self.fail(f'Got output:\n{actual}\nExpected:\n{expected}')
