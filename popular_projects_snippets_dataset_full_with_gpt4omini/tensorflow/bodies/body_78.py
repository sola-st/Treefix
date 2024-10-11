# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker_test.py
"""Test a set of configs that are empty or missing specification."""
self.compat_checker = compat_checker.ConfigCompatChecker(
    USER_CONFIG_MISSING, self.test_file)
# With missing specification in config file, the check should
# always fail.
self.assertFalse(self.compat_checker.check_compatibility())
