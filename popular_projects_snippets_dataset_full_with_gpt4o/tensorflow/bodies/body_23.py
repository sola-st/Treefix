# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
"""Diff given dicts of protobufs and report differences a readable way.

    Args:
      expected_dict: a dict of TFAPIObject protos constructed from golden files.
      actual_dict: a ict of TFAPIObject protos constructed by reading from the
        TF package linked to the test.
      verbose: Whether to log the full diffs, or simply report which files were
        different.
      update_goldens: Whether to update goldens when there are diffs found.
      additional_missing_object_message: Message to print when a symbol is
        missing.
      api_version: TensorFlow API version to test.
    """
diffs = []
verbose_diffs = []

expected_keys = set(expected_dict.keys())
actual_keys = set(actual_dict.keys())
only_in_expected = expected_keys - actual_keys
only_in_actual = actual_keys - expected_keys
all_keys = expected_keys | actual_keys

# This will be populated below.
updated_keys = []

for key in all_keys:
    diff_message = ''
    verbose_diff_message = ''
    # First check if the key is not found in one or the other.
    if key in only_in_expected:
        diff_message = 'Object %s expected but not found (removed). %s' % (
            key, additional_missing_object_message)
        verbose_diff_message = diff_message
    elif key in only_in_actual:
        diff_message = 'New object %s found (added).' % key
        verbose_diff_message = diff_message
    else:
        # Do not truncate diff
        self.maxDiff = None  # pylint: disable=invalid-name
        # Now we can run an actual proto diff.
        try:
            self.assertProtoEquals(expected_dict[key], actual_dict[key])
        except AssertionError as e:
            updated_keys.append(key)
            diff_message = 'Change detected in python object: %s.' % key
            verbose_diff_message = str(e)

      # All difference cases covered above. If any difference found, add to the
      # list.
    if diff_message:
        diffs.append(diff_message)
        verbose_diffs.append(verbose_diff_message)

    # If diffs are found, handle them based on flags.
if diffs:
    diff_count = len(diffs)
    logging.error(self._test_readme_message)
    logging.error('%d differences found between API and golden.', diff_count)

    if update_goldens:
        # Write files if requested.
        logging.warning(self._update_golden_warning)

        # If the keys are only in expected, some objects are deleted.
        # Remove files.
        for key in only_in_expected:
            filepath = _KeyToFilePath(key, api_version)
            file_io.delete_file(filepath)

        # If the files are only in actual (current library), these are new
        # modules. Write them to files. Also record all updates in files.
        for key in only_in_actual | set(updated_keys):
            filepath = _KeyToFilePath(key, api_version)
            file_io.write_string_to_file(
                filepath, text_format.MessageToString(actual_dict[key]))
    else:
        # Include the actual differences to help debugging.
        for d, verbose_d in zip(diffs, verbose_diffs):
            logging.error('    %s', d)
            logging.error('    %s', verbose_d)
        # Fail if we cannot fix the test by updating goldens.
        self.fail('%d differences found between API and golden.' % diff_count)

else:
    logging.info('No differences found between API and golden.')
