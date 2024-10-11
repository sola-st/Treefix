# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/linux/mkl/set-build-env.py
"""Set up argument parser, and parse CLI args."""
arg_parser = argparse.ArgumentParser(
    description="Parse the arguments for the "
    "TensorFlow build environment "
    " setter")
arg_parser.add_argument(
    "--disable-mkl",
    dest="disable_mkl",
    help="Turn off MKL. By default the compiler flag "
    "--config=mkl is enabled.",
    action="store_true")
arg_parser.add_argument(
    "--disable-v2",
    dest="disable_v2",
    help="Build TensorFlow v1 rather than v2. By default the "
    " compiler flag --config=v2 is enabled.",
    action="store_true")
arg_parser.add_argument(
    "--enable-bfloat16",
    dest="enable_bfloat16",
    help="Enable bfloat16 build. By default it is "
    " disabled if no parameter is passed.",
    action="store_true")
arg_parser.add_argument(
    "--enable-dnnl1",
    dest="enable_dnnl1",
    help="Enable dnnl1 build. By default it is "
    " disabled if no parameter is passed.",
    action="store_true")
arg_parser.add_argument(
    "-s",
    "--secure-build",
    dest="secure_build",
    help="Enable secure build flags.",
    action="store_true")
arg_parser.add_argument(
    "-p",
    "--platform",
    choices=self.PLATFORMS_.keys(),
    help="The target platform.",
    dest="target_platform",
    default=self.default_platform_)
arg_parser.add_argument(
    "-f",
    "--bazelrc-file",
    dest="bazelrc_file",
    help="The full path to the bazelrc file into which "
    "the build command will be written. The path "
    "will be relative to the container "
    " environment.",
    required=True)

self.args = arg_parser.parse_args()
