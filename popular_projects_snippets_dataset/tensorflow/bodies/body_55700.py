# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
with ops.Graph().as_default():
    local_op = constant_op.constant(42).op
    user_filename = "hope.py"
    modified_tb = _modify_op_stack_with_filenames(
        local_op.traceback,
        num_user_frames=3,
        user_filename=user_filename,
        num_inner_tf_frames=5)
    idx = error_interpolation._find_index_of_defining_frame(modified_tb)
    # Expected frame is 6th from the end because there are 5 inner frames with
    # TF filenames.
    expected_frame = len(modified_tb) - 6
    self.assertEqual(expected_frame, idx)
