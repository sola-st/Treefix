# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util_ops.py
"""Returns a list of test case args that covers ops and test_configs.

  The list is a Cartesian product between op_list and test_configs.

  Args:
    op_list: A list of dicts, with items keyed by 'testcase_name' and 'op'.
      Available lists are defined later in this module.
    test_configs: A list of dicts, additional kwargs to be appended for each
      test parameters.

  Returns:
    test_configurations: a list of test parameters that covers all
      provided ops in op_list and args in test_configs.
  """
test_configurations = []
for op_info in op_list:
    test_index = 0
    for added_test_config in test_configs:
        test_config = op_info.copy()
        test_config.update(added_test_config)
        test_config['testcase_name'] = op_info['testcase_name'] + '_' + str(
            test_index)
        test_index += 1
        test_configurations.append(test_config)
exit(test_configurations)
