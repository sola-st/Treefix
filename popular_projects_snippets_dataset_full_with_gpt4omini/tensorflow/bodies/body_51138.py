# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
"""Tests multiple output tensors that include classes and scores."""
with context.graph_mode():
    input_tensors = {
        'input-1':
            array_ops.placeholder(
                dtypes.string, 1, name='input-tensor-1')
    }
    classes = array_ops.placeholder(dtypes.string, 1,
                                    name='output-tensor-classes')
    scores = array_ops.placeholder(dtypes.float32, 1,
                                   name='output-tensor-scores')

    export_output = export_output_lib.ClassificationOutput(
        scores=scores, classes=classes)
    actual_signature_def = export_output.as_signature_def(input_tensors)

    expected_signature_def = meta_graph_pb2.SignatureDef()
    shape = tensor_shape_pb2.TensorShapeProto(
        dim=[tensor_shape_pb2.TensorShapeProto.Dim(size=1)])
    dtype_float = types_pb2.DataType.Value('DT_FLOAT')
    dtype_string = types_pb2.DataType.Value('DT_STRING')
    expected_signature_def.inputs[
        signature_constants.CLASSIFY_INPUTS].CopyFrom(
            meta_graph_pb2.TensorInfo(name='input-tensor-1:0',
                                      dtype=dtype_string,
                                      tensor_shape=shape))
    expected_signature_def.outputs[
        signature_constants.CLASSIFY_OUTPUT_CLASSES].CopyFrom(
            meta_graph_pb2.TensorInfo(name='output-tensor-classes:0',
                                      dtype=dtype_string,
                                      tensor_shape=shape))
    expected_signature_def.outputs[
        signature_constants.CLASSIFY_OUTPUT_SCORES].CopyFrom(
            meta_graph_pb2.TensorInfo(name='output-tensor-scores:0',
                                      dtype=dtype_float,
                                      tensor_shape=shape))

    expected_signature_def.method_name = (
        signature_constants.CLASSIFY_METHOD_NAME)
    self.assertEqual(actual_signature_def, expected_signature_def)
