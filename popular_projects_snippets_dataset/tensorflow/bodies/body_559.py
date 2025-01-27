# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/file_name_test.py
# Make sure BASE_DIR ends with tensorflow.  If it doesn't, we probably
# computed the wrong directory.
if os.path.split(BASE_DIR)[-1] != 'tensorflow':
    raise AssertionError(
        "BASE_DIR = '%s' doesn't end with tensorflow" % BASE_DIR)

for dirpath, dirnames, filenames in os.walk(BASE_DIR, followlinks=True):
    lowercase_directories = [x.lower() for x in dirnames]
    lowercase_files = [x.lower() for x in filenames]

    lowercase_dir_contents = lowercase_directories + lowercase_files
    if len(lowercase_dir_contents) != len(set(lowercase_dir_contents)):
        raise AssertionError(ERROR_MESSAGE.format(dirpath))
