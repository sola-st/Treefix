# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Verifies the max batch size annotations in the original and converted GraphDef.

    Args:
      expected_engines: A sequence of engines names.
      original_gdef: GraphDef. The graph def before TensorRT conversion.
      converted_gdef: GraphDef. The graph def after TensorRT conversion.
      default_max_batch_size: The default maximum batch size to use if no node
        inside a segment is annoted with a customized max batch size. This value
        is None when the graph is converted to TF-TRT with dynamic engines.
      expected_max_batch_sizes: Optional. A sequence of max batch sizes for all
        the engines. `None` if does not check enforce max batch sizes.
    """
if isinstance(expected_max_batch_sizes, collections.abc.Collection):
    self.assertEqual(len(expected_max_batch_sizes), len(expected_engines))
else:
    self.assertIsNone(
        expected_max_batch_sizes,
        "'expected_max_batch_sizes' shall only be a sequence "
        "of integers or `None`.")

def _ChainAllNodes(graph_def):
    exit(itertools.chain(
        graph_def.node,
        itertools.chain(
            *[func.node_def for func in graph_def.library.function])))

old_name_to_node_map = {
    self._ToString(node.name): node
    for node in _ChainAllNodes(original_gdef)
}
new_name_to_func_map = {
    self._ToString(func.signature.name): func
    for func in converted_gdef.library.function
}

def _DetectStaticBatchSize(node_def):
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

name_to_engines_map = {}
actual_max_batch_sizes = []
for node in _ChainAllNodes(converted_gdef):
    if node.op == "TRTEngineOp":
        engine = node
        engine_name = self._RemoveGraphSequenceNumber(
            self._Canonicalize(self._ToString(engine.name)))
        self.assertIn(engine_name, expected_engines)
        name_to_engines_map[engine_name] = engine
        # The input nodes shall not have the conflicting annotation (no
        # annotation or the same annotation) with the maximum batch size
        # annotation. If the engine has maximum batch size annotation as the
        # non-default maximum batch size, then at least one input node shall
        # have the same annotation to be the source.
        self.assertIn("max_batch_size", node.attr)
        engine_max_batch_size = node.attr["max_batch_size"].i
        self.assertIsInstance(engine_max_batch_size, int)
        actual_max_batch_sizes.append(engine_max_batch_size)
        seg_func = node.attr["segment_func"].func
        self.assertIsNotNone(seg_func)
        self.assertIn(seg_func.name, new_name_to_func_map)
        seg_func_def = new_name_to_func_map[seg_func.name]
        logging.info("Segment function name: %s. Including %d nodes.",
                     seg_func.name, len(seg_func_def.node_def))
        node_max_batch_size_all_none = True
        # Use the native segment to search for replaced nodes
        for alternative_node in seg_func_def.node_def:
            node_name = self._Canonicalize(self._ToString(alternative_node.name))
            if node_name not in old_name_to_node_map:
                continue
            original_node = old_name_to_node_map[node_name]
            node_max_batch_size = None
            if "_tftrt_op_max_batch_size" in original_node.attr:
                node_max_batch_size = original_node.attr[
                    "_tftrt_op_max_batch_size"].i
            elif (original_node.op != "Const" and
                  alternative_node.op != "Const" and
                  "_output_shapes" in original_node.attr):
                node_max_batch_size = _DetectStaticBatchSize(original_node)
            logging.info(
                "'{%s}(%s)'s max batch size annotation is %s. "
                "'{%s}'s max batch size is %s.", node_name, original_node.op,
                str(node_max_batch_size), engine_name, str(engine_max_batch_size))
            node_max_batch_size_all_none &= node_max_batch_size is None
            self.assertTrue(engine_max_batch_size == node_max_batch_size or
                            node_max_batch_size is None)
        logging.info("'{%s}'s max batch size is %d.", engine_name,
                     engine_max_batch_size)
        self.assertTrue(default_max_batch_size is None or
                        engine_max_batch_size == default_max_batch_size or
                        not node_max_batch_size_all_none)

self.assertCountEqual(expected_engines, tuple(name_to_engines_map.keys()))
if expected_max_batch_sizes is not None:
    self.assertCountEqual(expected_max_batch_sizes, actual_max_batch_sizes)
