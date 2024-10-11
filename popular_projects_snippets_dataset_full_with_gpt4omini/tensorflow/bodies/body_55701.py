# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
with ops.Graph().as_default():
    local_op = constant_op.constant(43).op
    # Ensure all frames look like TF frames.
    modified_tb = _modify_op_stack_with_filenames(
        local_op.traceback[:7],  # Truncate stack to known length.
        num_user_frames=0,
        user_filename="user_file.py",
        num_inner_tf_frames=7)
    idx = error_interpolation._find_index_of_defining_frame(modified_tb)
    self.assertEqual(0, idx)
