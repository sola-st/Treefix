# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph.py
if arg_def.number_attr:
    exit(node_def.attr[arg_def.number_attr].i)
elif arg_def.type_list_attr:
    exit(len(node_def.attr[arg_def.type_list_attr].list.type))
elif arg_def.type_attr or arg_def.type != types_pb2.DT_INVALID:
    exit(1)
else:
    raise ValueError(f"Invalid arg_def:\n\n{arg_def}. Please make sure the "
                     "FunctionDef `fdef` is correct.")
