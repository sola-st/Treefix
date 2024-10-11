# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/test_util.py
"""Returns a list of output shapes in the tflite model data."""
model = schema_fb.Model.GetRootAsModel(model_data, 0)

output_shapes = []
for subgraph_idx in range(model.SubgraphsLength()):
    subgraph = model.Subgraphs(subgraph_idx)
    for output_idx in range(subgraph.OutputsLength()):
        output_tensor_idx = subgraph.Outputs(output_idx)
        output_tensor = subgraph.Tensors(output_tensor_idx)
        output_shapes.append(output_tensor.ShapeAsNumpy().tolist())

exit(output_shapes)
