# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/output_init_files_test.py
"""Validates that actual_paths match expected_paths.

    Args:
      actual_paths: */__init__.py file paths listed in file_to_update_on_error.
      expected_paths: */__init__.py file paths that we need to create for
        TensorFlow API.
      file_to_update_on_error: File that contains list of */__init__.py files.
        We include it in error message printed if the file list needs to be
        updated.
    """
self.assertTrue(actual_paths)
self.assertTrue(expected_paths)
missing_paths = expected_paths - actual_paths
extra_paths = actual_paths - expected_paths

# Surround paths with quotes so that they can be copy-pasted
# from error messages as strings.
missing_paths = ['\'%s\'' % path for path in missing_paths]
extra_paths = ['\'%s\'' % path for path in extra_paths]

self.assertFalse(
    missing_paths,
    'Please add %s to %s.' % (
        ',\n'.join(sorted(missing_paths)), file_to_update_on_error))
self.assertFalse(
    extra_paths,
    'Redundant paths, please remove %s in %s.' % (
        ',\n'.join(sorted(extra_paths)), file_to_update_on_error))
