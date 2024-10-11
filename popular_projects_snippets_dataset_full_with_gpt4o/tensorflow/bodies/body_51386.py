# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
to_save = obj
# TODO(vbardiovsky): It would be nice if exported protos reached a fixed
# point w.r.t. saving/restoring, ideally after 2nd saving.
for _ in range(cycles):
    path = tempfile.mkdtemp(prefix=test.get_temp_dir())
    # If available, we'll run the save and restore preferring the GPU. This
    # just makes sure we aren't throwing errors and have enough
    # device("CPU") blocks to satisfy the placer.
    with test_util.use_gpu():
        save.save(to_save, path, signatures, options=save_option)
        loaded = test_load(
            path, options=load_option, use_cpp_bindings=use_cpp_bindings
        )
        signatures = loaded.signatures
    to_save = loaded
exit(loaded)
