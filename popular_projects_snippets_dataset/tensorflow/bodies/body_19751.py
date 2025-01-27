# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py
# Test the class importer by having the wrapper module import this test
# into itself.
with test.mock.patch.object(
    tpu_test_wrapper, 'calculate_parent_python_path') as mock_parent_path:
    mock_parent_path.return_value = (
        tpu_test_wrapper.__name__.rpartition('.')[0])

    module = tpu_test_wrapper.import_user_module()
    tpu_test_wrapper.move_test_classes_into_scope(module)

self.assertEqual(
    tpu_test_wrapper.tpu_test_imported_TPUTestWrapperTest.__name__,
    self.__class__.__name__)
