# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_control_flow_illegal_cases_test.py
with self.assertRaisesRegex(
    NotImplementedError,
    re.compile(
        r'.*condition of while loop started as non\-Tensor,'
        r' then changed to Tensor.*', re.DOTALL)):
    tf.function(target)(n)
