# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
if node.op == "StatefulPartitionedCall":
    fn_name = node.attr["f"].func.name
    if fn_name.startswith("__inference_f"):
        self.assertLen(node.attr["_output_shapes"].list.shape, 2)
    if fn_name.startswith("__inference_g"):
        self.assertLen(node.attr["_output_shapes"].list.shape, 1)
