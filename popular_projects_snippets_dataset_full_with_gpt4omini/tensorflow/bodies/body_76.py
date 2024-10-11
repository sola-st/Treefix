# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker_test.py
"""Test a set of configs that are supported.

    Testing with the following combination should always return `success`:
      [1] A set of configurations that are supported and/or compatible.
      [2] `.ini` config file with proper formatting.
    """
# Initialize compatibility checker.
self.compat_checker = compat_checker.ConfigCompatChecker(
    USER_CONFIG_IN_RANGE, self.test_file)
# Compatibility check should succeed.
self.assertTrue(self.compat_checker.check_compatibility())
# Make sure no warning or error messages are recorded.
self.assertFalse(len(self.compat_checker.error_msg))
# Make sure total # of successes match total # of configs.
cnt = len(list(USER_CONFIG_IN_RANGE.keys()))
self.assertEqual(len(self.compat_checker.successes), cnt)
