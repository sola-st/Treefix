# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker_test.py
"""Test a set of configs that are NOT supported.

    Testing with the following combination should always return `failure`:
      [1] A set of configurations that are NOT supported and/or compatible.
      [2] `.ini` config file with proper formatting.
    """
self.compat_checker = compat_checker.ConfigCompatChecker(
    USER_CONFIG_NOT_IN_RANGE, self.test_file)
# Compatibility check should fail.
self.assertFalse(self.compat_checker.check_compatibility())
# Check error and warning messages.
err_msg_list = self.compat_checker.failures
self.assertTrue(len(err_msg_list))
# Make sure total # of failures match total # of configs.
cnt = len(list(USER_CONFIG_NOT_IN_RANGE.keys()))
self.assertEqual(len(err_msg_list), cnt)
