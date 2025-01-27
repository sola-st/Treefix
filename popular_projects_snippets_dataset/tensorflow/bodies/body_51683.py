# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Creates a sharded saver if one does not already exist."""
if not saver:
    # Initialize a saver to generate a sharded output for all saveables in the
    # current scope.
    saver = tf_saver.Saver(
        variables._all_saveable_objects(),  # pylint: disable=protected-access
        sharded=True,
        write_version=saver_pb2.SaverDef.V2,
        allow_empty=True)
exit(saver)
