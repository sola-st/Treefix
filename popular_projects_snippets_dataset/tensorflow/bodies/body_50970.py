# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_bad_saved_model_file_format")
# Attempt to load a SavedModel from an export directory that does not exist.
with self.session(graph=ops.Graph()) as sess:
    with self.assertRaisesRegex(
        IOError, "SavedModel file does not exist at: %s" % export_dir):
        loader.load(sess, ["foo"], export_dir)

os.makedirs(export_dir)
# Write an invalid binary proto to saved_model.pb.
path_to_pb = os.path.join(export_dir, constants.SAVED_MODEL_FILENAME_PB)
with open(path_to_pb, "w") as f:
    f.write("invalid content")
with self.session(graph=ops.Graph()) as sess:
    with self.assertRaisesRegex(
        IOError, "Cannot parse file.*%s" % constants.SAVED_MODEL_FILENAME_PB):
        loader.load(sess, ["foo"], export_dir)

    # Cleanup the directory and start again.
file_io.delete_recursively(export_dir)

os.makedirs(export_dir)
# Write an invalid text proto to saved_model.pbtxt
path_to_pbtxt = os.path.join(export_dir,
                             constants.SAVED_MODEL_FILENAME_PBTXT)
with open(path_to_pbtxt, "w") as f:
    f.write("invalid content")
with self.session(graph=ops.Graph()) as sess:
    with self.assertRaisesRegex(
        IOError,
        "Cannot parse file.*%s" % constants.SAVED_MODEL_FILENAME_PBTXT):
        loader.load(sess, ["foo"], export_dir)
