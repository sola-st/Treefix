# Extracted from ./data/repos/tensorflow/tensorflow/lite/ios/extract_object_files.py
"""Extracts object files from the archive path to the destination directory.

  Extracts object files from the given BSD variant archive file. The extracted
  files are written to the destination directory, which will be created if the
  directory does not exist.

  Colliding object file names are automatically renamed upon extraction in order
  to avoid unintended overwriting.

  Args:
    archive_file: The archive file object pointing at its beginning.
    dest_dir: The destination directory path in which the extracted object files
      will be written. The directory will be created if it does not exist.
  """
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

_check_archive_signature(archive_file)

# Keep the extracted file names and their content hash values, in order to
# handle duplicate names correctly.
extracted_files = dict()

for name, file_content in _extract_next_file(archive_file):
    digest = hashlib.md5(file_content).digest()

    # Check if the name is already used. If so, come up with a different name by
    # incrementing the number suffix until it finds an unused one.
    # For example, if 'foo.o' is used, try 'foo_1.o', 'foo_2.o', and so on.
    for final_name in _generate_modified_filenames(name):
        if final_name not in extracted_files:
            extracted_files[final_name] = digest

            # Write the file content to the desired final path.
            with open(os.path.join(dest_dir, final_name), 'wb') as object_file:
                object_file.write(file_content)
            break

        # Skip writing this file if the same file was already extracted.
        elif extracted_files[final_name] == digest:
            break
