# Extracted from ./data/repos/tensorflow/tensorflow/tools/gcs_test/python/gcs_smoke.py
"""Verifies file_io's object manipulation methods ."""
starttime_ms = int(round(time.time() * 1000))
dir_name = "%s/tf_gcs_test_%s" % (FLAGS.gcs_bucket_url, starttime_ms)
print("Creating dir %s." % dir_name)
file_io.create_dir(dir_name)

num_files = 5
# Create files of 2 different patterns in this directory.
files_pattern_1 = ["%s/test_file_%d.txt" % (dir_name, n)
                   for n in range(num_files)]
files_pattern_2 = ["%s/testfile%d.txt" % (dir_name, n)
                   for n in range(num_files)]

starttime_ms = int(round(time.time() * 1000))
files_to_create = files_pattern_1 + files_pattern_2
for file_name in files_to_create:
    print("Creating file %s." % file_name)
    file_io.write_string_to_file(file_name, "test file creation.")
elapsed_ms = int(round(time.time() * 1000)) - starttime_ms
print("Created %d files in %s milliseconds" % (
    len(files_to_create), elapsed_ms))

# Listing files of pattern1.
list_files_pattern = "%s/test_file*.txt" % dir_name
print("Getting files matching pattern %s." % list_files_pattern)
starttime_ms = int(round(time.time() * 1000))
files_list = file_io.get_matching_files(list_files_pattern)
elapsed_ms = int(round(time.time() * 1000)) - starttime_ms
print("Listed files in %s milliseconds" % elapsed_ms)
print(files_list)
assert set(files_list) == set(files_pattern_1)

# Listing files of pattern2.
list_files_pattern = "%s/testfile*.txt" % dir_name
print("Getting files matching pattern %s." % list_files_pattern)
starttime_ms = int(round(time.time() * 1000))
files_list = file_io.get_matching_files(list_files_pattern)
elapsed_ms = int(round(time.time() * 1000)) - starttime_ms
print("Listed files in %s milliseconds" % elapsed_ms)
print(files_list)
assert set(files_list) == set(files_pattern_2)

# Test renaming file.
file_to_rename = "%s/oldname.txt" % dir_name
file_new_name = "%s/newname.txt" % dir_name
file_io.write_string_to_file(file_to_rename, "test file.")
assert file_io.file_exists(file_to_rename)
assert not file_io.file_exists(file_new_name)

print("Will try renaming file %s to %s" % (file_to_rename, file_new_name))
starttime_ms = int(round(time.time() * 1000))
file_io.rename(file_to_rename, file_new_name)
elapsed_ms = int(round(time.time() * 1000)) - starttime_ms
print("File %s renamed to %s in %s milliseconds" % (
    file_to_rename, file_new_name, elapsed_ms))
assert not file_io.file_exists(file_to_rename)
assert file_io.file_exists(file_new_name)

# Delete directory.
print("Deleting directory %s." % dir_name)
file_io.delete_recursively(dir_name)
