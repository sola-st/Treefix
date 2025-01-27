# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
self.assertEqual(
    expected_result,
    linear_operator_util.use_operator_or_provided_hint_unless_contradicting(
        operator=DummyOperatorWithHint(my_hint=operator_hint_value),
        hint_attr_name="my_hint",
        provided_hint_value=provided_hint_value,
        message="should not be needed here"))
