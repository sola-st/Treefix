# Extracted from ./data/repos/tensorflow/tensorflow/lite/ios/extract_object_files_test.py
with io.BytesIO(b'this is an invalid archive file') as archive_file:
    with self.assertRaises(RuntimeError):
        extract_object_files.extract_object_files(
            archive_file,
            self.create_tempdir().full_path)
