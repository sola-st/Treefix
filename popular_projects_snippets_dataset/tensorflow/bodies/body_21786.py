# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
shape_list = [tensor_shape.as_shape(s) for s in shape_list]
if enqueue_many:
    # We want the shapes without the leading batch dimension.
    shape_list = [s.with_rank_at_least(1)[1:] for s in shape_list]
merged_shape = shape_list[0]
for s in shape_list[1:]:
    merged_shape.merge_with(s)
exit(merged_shape.as_list())
