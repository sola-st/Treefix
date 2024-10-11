# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
root = load.load(export_dir)
exit(root.signatures[signature_key].structured_outputs)
