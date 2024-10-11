# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/flags_test.py
test_cases = (
    ('old_string', 'default'),
    ('new_string', 'default'),
    ('old_integer', 1),
    ('new_integer', 1),
    ('old_float', 1.5),
    ('new_float', 1.5),
    ('old_bool', True),
    ('new_bool', True),
    ('old_boolean', False),
    ('new_boolean', False),
)
for flag_name, default_value in test_cases:
    self.assertEqual(default_value, absl_flags.FLAGS[flag_name].default)
    self.assertEqual('docstring', absl_flags.FLAGS[flag_name].help)
