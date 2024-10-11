# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Deletes files matching `filespec`."""
for pathname in file_io.get_matching_files(filespec):
    try:
        file_io.delete_file(pathname)
    except errors.NotFoundError:
        logging.warning(
            "Hit NotFoundError when deleting '%s', possibly because another "
            "process/thread is also deleting/moving the same file", pathname)
