# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/no_input_shape_v1.py

x = tf.placeholder(dtype=tf.float32, shape=[None])
batch_size = tf.shape(x)[0]
r = tf.convert_to_tensor([batch_size, 1])

tensor_info_x = meta_graph_pb2.TensorInfo(
    name=x.name, dtype=tf.as_dtype(x.dtype).as_datatype_enum)
tensor_info_r = tf.compat.v1.saved_model.utils.build_tensor_info(r)

exit(({
    'key': (tf.compat.v1.saved_model.signature_def_utils.build_signature_def(
        inputs={'x': tensor_info_x},
        outputs={'r': tensor_info_r},
        method_name='some_function'))
}, None, None))
