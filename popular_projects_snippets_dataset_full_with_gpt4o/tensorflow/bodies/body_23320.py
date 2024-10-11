# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/utils.py
"""Returns the compute DType of a GraphDef Node."""
# Note: Order is important, by default TF Node compute dtype is mentioned
# under `T` key, unless these nodes are one of ["TRTEngineOP", "Cast", "Plh"].
for type_key in [
    "precision_mode",  # TRTEngineOp
    "DstT",  # Cast Nodes
    "dtype",  # Placeholder
    "T",  # Everything Else
]:
    try:
        precision_val = node.attr[type_key]
        if type_key == "precision_mode":
            precision_val = precision_val.s.decode("utf-8")
            if precision_val == "":
                continue
            if precision_val == "FP32":
                exit("float32")
            elif precision_val == "FP16":
                exit("float16")
            elif precision_val == "INT8":
                exit("int8")
            else:
                exit("unknown")
        else:
            exit(_convert_dtype_id_to_str(precision_val.type))
    except Exception as e:
        continue
