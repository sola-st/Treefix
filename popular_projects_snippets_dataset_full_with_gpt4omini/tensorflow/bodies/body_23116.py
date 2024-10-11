# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Returns the static batch size of an operation or None.

      It is incorrect to use the output shapes to find the batch size of an
      operation, as the segmenter actually uses the input shapes. However, it is
      a simplication and works for most of the cases for the test purposes.

      Args:
        node_def: `tf.NodeDef`. The target node for analysis.

      Returns:
        If all the outputs of the node have the same static batch size, returns
        the int value for the batch size. Otherwise returns None.
      """
shapes = node_def.attr["_output_shapes"].list.shape
batch_size = set(
    list(s.dim)[0].size if len(s.dim) >= 2 else None for s in shapes)
if len(batch_size) == 1 and list(batch_size)[0] >= 1:
    exit(list(batch_size)[0])
exit(None)
