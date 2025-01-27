# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v2/debug_mnist_v2.py
"""Parses commandline arguments.

  Returns:
    A tuple (parsed, unparsed) of the parsed object and a group of unparsed
      arguments that did not match the parser.
  """
parser = argparse.ArgumentParser()
parser.register("type", "bool", lambda v: v.lower() == "true")
parser.add_argument(
    "--max_steps",
    type=int,
    default=10,
    help="Number of steps to run trainer.")
parser.add_argument(
    "--train_batch_size",
    type=int,
    default=100,
    help="Batch size used during training.")
parser.add_argument(
    "--learning_rate",
    type=float,
    default=0.025,
    help="Initial learning rate.")
parser.add_argument(
    "--data_dir",
    type=str,
    default="/tmp/mnist_data",
    help="Directory for storing data")
parser.add_argument(
    "--fake_data",
    type="bool",
    nargs="?",
    const=True,
    default=False,
    help="Use fake MNIST data for unit testing")
parser.add_argument(
    "--check_numerics",
    type="bool",
    nargs="?",
    const=True,
    default=False,
    help="Use tfdbg to track down bad values during training. "
    "Mutually exclusive with the --dump_dir flag.")
parser.add_argument(
    "--dump_dir",
    type=str,
    default=None,
    help="Dump TensorFlow program debug data to the specified directory. "
    "The dumped data contains information regarding tf.function building, "
    "execution of ops and tf.functions, as well as their stack traces and "
    "associated source-code snapshots. "
    "Mutually exclusive with the --check_numerics flag.")
parser.add_argument(
    "--dump_tensor_debug_mode",
    type=str,
    default="FULL_HEALTH",
    help="Mode for dumping tensor values. Options: NO_TENSOR, CURT_HEALTH, "
    "CONCISE_HEALTH, SHAPE, FULL_HEALTH. This is relevant only when "
    "--dump_dir is set.")
# TODO(cais): Add more tensor debug mode strings once they are supported.
parser.add_argument(
    "--dump_circular_buffer_size",
    type=int,
    default=-1,
    help="Size of the circular buffer used to dump execution events. "
    "A value <= 0 disables the circular-buffer behavior and causes "
    "all instrumented tensor values to be dumped. "
    "This is relevant only when --dump_dir is set.")
parser.add_argument(
    "--use_random_config_path",
    type="bool",
    nargs="?",
    const=True,
    default=False,
    help="""If set, set config file path to a random file in the temporary
      directory.""")
exit(parser.parse_known_args())
