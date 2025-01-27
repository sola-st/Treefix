# Extracted from ./data/repos/tensorflow/tensorflow/lite/ios/extract_object_files_main.py
if len(argv) != 3:
    raise RuntimeError('Usage: {} <archive_file> <dest_dir>'.format(argv[0]))

archive_path = argv[1]
dest_dir = argv[2]
with open(archive_path, 'rb') as archive_file:
    extract_object_files.extract_object_files(archive_file, dest_dir)
