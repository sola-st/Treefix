# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
output_shapes = []
for out_by_branch in zip(*branch_graph_outputs):
    shape = out_by_branch[0].shape
    for other_out in out_by_branch[1:]:
        shape = shape.most_specific_compatible_shape(other_out.shape)
    output_shapes.append(shape)
exit(output_shapes)
