# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""This method describes the results of the conversion by TF-TRT.

    It includes information such as the name of the engine, the number of nodes
    per engine, the input and output dtype, along with the input shape of each
    TRTEngineOp.

    Args:
      line_length: Default line length when printing on the console. Minimum 160
        characters long.
      detailed: Whether or not to show the nodes inside each TRTEngineOp.
      print_fn: Print function to use. Defaults to `print`. It will be called on
        each line of the summary. You can set it to a custom function in order
        to capture the string summary.

    Raises:
      RuntimeError: if the graph is not converted.
    """
if not self._converted:
    raise RuntimeError(
        f"Impossible to call `{self.__class__.__name__}.summary()` before "
        f"calling {self.__class__.__name__}.convert()`.")

if line_length < 160:
    raise ValueError(f"Invalid `line_length` value has been received: "
                     f"{line_length}. Minimum: 160.")

if print_fn is None:
    print_fn = print

# positions are percentage of `line_length`. positions[i]+1 is the starting
# position for (i+1)th field. We also make sure that the last char printed
# for each field is a space.
columns = [
    # (column name, column size in % of line)
    ("TRTEngineOP Name", .20),  # 20%
    ("Device", .09),  # 29%
    ("# Nodes", .05),  # 34%
    ("# Inputs", .09),  # 43%
    ("# Outputs", .09),  # 52%
    ("Input DTypes", .12),  # 64%
    ("Output Dtypes", .12),  # 76%
    ("Input Shapes", .12),  # 88%
    ("Output Shapes", .12)  # 100%
]

positions = [int(line_length * p) for _, p in columns]
positions = np.cumsum(positions).tolist()
headers = [h for h, _ in columns]

_print_row(headers, positions, print_fn=print_fn)
print_fn("=" * line_length)

n_engines = 0
n_ops_converted = 0
n_ops_not_converted = 0

graphdef = self._converted_func.graph.as_graph_def(add_shapes=True)

trtengineops_dict = dict()
for node in graphdef.node:
    if node.op != "TRTEngineOp":
        n_ops_not_converted += 1
        continue
    else:
        trtengineops_dict[node.name] = node
        n_engines += 1

for name, node in sorted(trtengineops_dict.items()):
    node_device = node.device.split("/")[-1]
    in_shapes = trt_utils.get_node_io_shapes(node, "input_shapes")
    out_shapes = trt_utils.get_node_io_shapes(node, "_output_shapes")
    in_dtypes = trt_utils.get_trtengineop_io_dtypes(node, "InT")
    out_dtypes = trt_utils.get_trtengineop_io_dtypes(node, "OutT")
    in_nodes_count = trt_utils.get_trtengineop_io_nodes_count(node, "InT")
    out_nodes_count = trt_utils.get_trtengineop_io_nodes_count(node, "OutT")
    node_count, converted_ops_dict = trt_utils.get_trtengineop_node_op_count(
        graphdef, name)

    n_ops_converted += node_count

    if n_engines != 1:
        print_fn(f"\n{'-'*40}\n")

    _print_row(
        fields=[
            name, node_device, node_count, in_nodes_count, out_nodes_count,
            in_dtypes, out_dtypes, in_shapes, out_shapes
        ],
        positions=positions,
        print_fn=print_fn)

    if detailed:
        print_fn()
        for key, value in sorted(dict(converted_ops_dict).items()):
            print_fn(f"\t- {key}: {value}x")

print_fn(f"\n{'='*line_length}")
print_fn(f"[*] Total number of TensorRT engines: {n_engines}")
total_ops = n_ops_not_converted + n_ops_converted
conversion_ratio = n_ops_converted / total_ops * 100
print_fn(f"[*] % of OPs Converted: {conversion_ratio:.2f}% "
         f"[{n_ops_converted}/{total_ops}]\n")
