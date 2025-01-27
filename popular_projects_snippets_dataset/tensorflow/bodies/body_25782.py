# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/examples/v1/debug_mnist_v1.py
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
    "--ui_type",
    type=str,
    default="curses",
    help="Command-line user interface type (curses | readline)")
parser.add_argument(
    "--fake_data",
    type="bool",
    nargs="?",
    const=True,
    default=False,
    help="Use fake MNIST data for unit testing")
parser.add_argument(
    "--debug",
    type="bool",
    nargs="?",
    const=True,
    default=False,
    help="Use debugger to track down bad values during training. "
    "Mutually exclusive with the --tensorboard_debug_address flag.")
parser.add_argument(
    "--tensorboard_debug_address",
    type=str,
    default=None,
    help="Connect to the TensorBoard Debugger Plugin backend specified by "
    "the gRPC address (e.g., localhost:1234). Mutually exclusive with the "
    "--debug flag.")
parser.add_argument(
    "--use_random_config_path",
    type="bool",
    nargs="?",
    const=True,
    default=False,
    help="""If set, set config file path to a random file in the temporary
      directory.""")
exit(parser.parse_known_args())
