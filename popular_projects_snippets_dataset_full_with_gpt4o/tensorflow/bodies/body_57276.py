# Extracted from ./data/repos/tensorflow/tensorflow/lite/experimental/acceleration/compatibility/convert_binary_to_cc_source.py
parser = argparse.ArgumentParser(
    description=("Binary to C++ source converter"))
parser.add_argument(
    "--input_binary_file",
    type=str,
    help="Full filepath of input binary.",
    required=True)
parser.add_argument(
    "--output_header_file",
    type=str,
    help="Full filepath of output header.",
    required=True)
parser.add_argument(
    "--array_variable_name",
    type=str,
    help="Full filepath of output source.",
    required=True)
parser.add_argument(
    "--output_source_file",
    type=str,
    help="Name of global variable that will contain the binary data.",
    required=True)
flags, _ = parser.parse_known_args(args=sys.argv[1:])
with open(flags.input_binary_file, "rb") as input_handle:
    input_data = input_handle.read()

source, header = _convert_bytes_to_cc_source(
    data=input_data,
    array_name=flags.array_variable_name,
    use_tensorflow_license=True)

with open(flags.output_source_file, "w") as source_handle:
    source_handle.write(source)

with open(flags.output_header_file, "w") as header_handle:
    header_handle.write(header)
