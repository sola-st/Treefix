# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
exit(tensor_name if output_index == 0 else "%s:%d" % (tensor_name,
                                                        output_index))
