# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
super(ApiCompatibilityTest, self).__init__(*args, **kwargs)

golden_update_warning_filename = os.path.join(
    resource_loader.get_root_dir_with_all_resources(), _UPDATE_WARNING_FILE)
self._update_golden_warning = file_io.read_file_to_string(
    golden_update_warning_filename)

test_readme_filename = os.path.join(
    resource_loader.get_root_dir_with_all_resources(), _TEST_README_FILE)
self._test_readme_message = file_io.read_file_to_string(
    test_readme_filename)
