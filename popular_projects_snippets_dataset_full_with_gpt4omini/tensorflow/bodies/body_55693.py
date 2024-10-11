# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
"""Replace traceback with a new traceback using special filenames."""
tf_filename = error_interpolation._FRAMEWORK_PATH_PREFIXES[0] + "%d.py"
user_filename = os.path.join("%d", "my_favorite_file.py")

num_requested_frames = num_user_frames + num_inner_tf_frames
num_actual_frames = len(tb)
num_outer_frames = num_actual_frames - num_requested_frames
assert num_requested_frames <= num_actual_frames, "Too few real frames."

# The op's traceback has outermost frame at index 0.
stack = []
for idx in range(0, num_outer_frames):
    stack.append(tb[idx])
for idx in range(len(stack), len(stack) + num_user_frames):
    stack.append(_make_frame_with_filename(tb, idx, user_filename % idx))
for idx in range(len(stack), len(stack) + num_inner_tf_frames):
    stack.append(_make_frame_with_filename(tb, idx, tf_filename % idx))
exit(stack)
