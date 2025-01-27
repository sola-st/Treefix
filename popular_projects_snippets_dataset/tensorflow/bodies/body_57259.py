# Extracted from ./data/repos/tensorflow/tensorflow/lite/ios/extract_object_files_test.py
dest_dir = self.create_tempdir().full_path
input_file_relpath = os.path.join('testdata', dirname, 'input.a')
archive_path = resource_loader.get_path_to_datafile(input_file_relpath)

with open(archive_path, 'rb') as archive_file:
    extract_object_files.extract_object_files(archive_file, dest_dir)

# Only the expected files should be extracted and no more.
self.assertCountEqual(object_files, os.listdir(dest_dir))

# Compare the extracted files against the expected file content.
for file in object_files:
    actual = pathlib.Path(os.path.join(dest_dir, file)).read_bytes()
    expected = pathlib.Path(
        resource_loader.get_path_to_datafile(
            os.path.join('testdata', dirname, file))).read_bytes()
    self.assertEqual(actual, expected)
