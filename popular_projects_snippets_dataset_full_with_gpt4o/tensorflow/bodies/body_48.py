# Extracted from ./data/repos/tensorflow/tensorflow/tools/gcs_test/python/gcs_smoke.py
"""Verifies file_io directory handling methods."""

# Test directory creation.
starttime_ms = int(round(time.time() * 1000))
dir_name = "%s/tf_gcs_test_%s" % (FLAGS.gcs_bucket_url, starttime_ms)
print("Creating dir %s" % dir_name)
file_io.create_dir(dir_name)
elapsed_ms = int(round(time.time() * 1000)) - starttime_ms
print("Created directory in: %d milliseconds" % elapsed_ms)

# Check that the directory exists.
dir_exists = file_io.is_directory(dir_name)
assert dir_exists
print("%s directory exists: %s" % (dir_name, dir_exists))

# Test recursive directory creation.
starttime_ms = int(round(time.time() * 1000))
recursive_dir_name = "%s/%s/%s" % (dir_name,
                                   "nested_dir1",
                                   "nested_dir2")
print("Creating recursive dir %s" % recursive_dir_name)
file_io.recursive_create_dir(recursive_dir_name)
elapsed_ms = int(round(time.time() * 1000)) - starttime_ms
print("Created directory recursively in: %d milliseconds" % elapsed_ms)

# Check that the directory exists.
recursive_dir_exists = file_io.is_directory(recursive_dir_name)
assert recursive_dir_exists
print("%s directory exists: %s" % (recursive_dir_name, recursive_dir_exists))

# Create some contents in the just created directory and list the contents.
num_files = 10
files_to_create = ["file_%d.txt" % n for n in range(num_files)]
for file_num in files_to_create:
    file_name = "%s/%s" % (dir_name, file_num)
    print("Creating file %s." % file_name)
    file_io.write_string_to_file(file_name, "test file.")

print("Listing directory %s." % dir_name)
starttime_ms = int(round(time.time() * 1000))
directory_contents = file_io.list_directory(dir_name)
print(directory_contents)
elapsed_ms = int(round(time.time() * 1000)) - starttime_ms
print("Listed directory %s in %s milliseconds" % (dir_name, elapsed_ms))
assert set(directory_contents) == set(files_to_create + ["nested_dir1/"])

# Test directory renaming.
dir_to_rename = "%s/old_dir" % dir_name
new_dir_name = "%s/new_dir" % dir_name
file_io.create_dir(dir_to_rename)
assert file_io.is_directory(dir_to_rename)
assert not file_io.is_directory(new_dir_name)

starttime_ms = int(round(time.time() * 1000))
print("Will try renaming directory %s to %s" % (dir_to_rename, new_dir_name))
file_io.rename(dir_to_rename, new_dir_name)
elapsed_ms = int(round(time.time() * 1000)) - starttime_ms
print("Renamed directory %s to %s in %s milliseconds" % (
    dir_to_rename, new_dir_name, elapsed_ms))
assert not file_io.is_directory(dir_to_rename)
assert file_io.is_directory(new_dir_name)

# Test Delete directory recursively.
print("Deleting directory recursively %s." % dir_name)
starttime_ms = int(round(time.time() * 1000))
file_io.delete_recursively(dir_name)
elapsed_ms = int(round(time.time() * 1000)) - starttime_ms
dir_exists = file_io.is_directory(dir_name)
assert not dir_exists
print("Deleted directory recursively %s in %s milliseconds" % (
    dir_name, elapsed_ms))
