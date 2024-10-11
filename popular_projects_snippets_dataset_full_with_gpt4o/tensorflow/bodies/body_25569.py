# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
"""ProfileAnalyzer constructor.

    Args:
      graph: (tf.Graph) Python graph object.
      run_metadata: A `RunMetadata` protobuf object.

    Raises:
      ValueError: If run_metadata is None.
    """
self._graph = graph
if not run_metadata:
    raise ValueError("No RunMetadata passed for profile analysis.")
self._run_metadata = run_metadata
self._arg_parsers = {}
ap = argparse.ArgumentParser(
    description="List nodes profile information.",
    usage=argparse.SUPPRESS)
ap.add_argument(
    "-d",
    "--%s" % _DEVICE_NAME_FILTER_FLAG,
    dest=_DEVICE_NAME_FILTER_FLAG,
    type=str,
    default="",
    help="filter device name by regex.")
ap.add_argument(
    "-n",
    "--%s" % _NODE_NAME_FILTER_FLAG,
    dest=_NODE_NAME_FILTER_FLAG,
    type=str,
    default="",
    help="filter node name by regex.")
ap.add_argument(
    "-t",
    "--%s" % _OP_TYPE_FILTER_FLAG,
    dest=_OP_TYPE_FILTER_FLAG,
    type=str,
    default="",
    help="filter op type by regex.")
# TODO(annarev): allow file filtering at non-stack top position.
ap.add_argument(
    "-f",
    "--file_path_filter",
    dest="file_path_filter",
    type=str,
    default="",
    help="filter by file name at the top position of node's creation "
         "stack that does not belong to TensorFlow library.")
ap.add_argument(
    "--min_lineno",
    dest="min_lineno",
    type=int,
    default=-1,
    help="(Inclusive) lower bound for 1-based line number in source file. "
         "If <= 0, has no effect.")
ap.add_argument(
    "--max_lineno",
    dest="max_lineno",
    type=int,
    default=-1,
    help="(Exclusive) upper bound for 1-based line number in source file. "
         "If <= 0, has no effect.")
ap.add_argument(
    "-e",
    "--execution_time",
    dest="execution_time",
    type=str,
    default="",
    help="Filter by execution time interval "
         "(includes compute plus pre- and post -processing time). "
         "Supported units are s, ms and us (default). "
         "E.g. -e >100s, -e <100, -e [100us,1000ms]")
ap.add_argument(
    "-o",
    "--op_time",
    dest="op_time",
    type=str,
    default="",
    help="Filter by op time interval (only includes compute time). "
         "Supported units are s, ms and us (default). "
         "E.g. -e >100s, -e <100, -e [100us,1000ms]")
ap.add_argument(
    "-s",
    "--sort_by",
    dest="sort_by",
    type=str,
    default=SORT_OPS_BY_START_TIME,
    help=("the field to sort the data by: (%s)" %
          " | ".join([SORT_OPS_BY_OP_NAME, SORT_OPS_BY_OP_TYPE,
                      SORT_OPS_BY_START_TIME, SORT_OPS_BY_OP_TIME,
                      SORT_OPS_BY_EXEC_TIME, SORT_OPS_BY_LINE])))
ap.add_argument(
    "-r",
    "--reverse",
    dest="reverse",
    action="store_true",
    help="sort the data in reverse (descending) order")
ap.add_argument(
    "--time_unit",
    dest="time_unit",
    type=str,
    default=cli_shared.TIME_UNIT_US,
    help="Time unit (" + " | ".join(cli_shared.TIME_UNITS) + ")")

self._arg_parsers["list_profile"] = ap

ap = argparse.ArgumentParser(
    description="Print a Python source file with line-level profile "
                "information",
    usage=argparse.SUPPRESS)
ap.add_argument(
    "source_file_path",
    type=str,
    help="Path to the source_file_path")
ap.add_argument(
    "--cost_type",
    type=str,
    choices=["exec_time", "op_time"],
    default="exec_time",
    help="Type of cost to display")
ap.add_argument(
    "--time_unit",
    dest="time_unit",
    type=str,
    default=cli_shared.TIME_UNIT_US,
    help="Time unit (" + " | ".join(cli_shared.TIME_UNITS) + ")")
ap.add_argument(
    "-d",
    "--%s" % _DEVICE_NAME_FILTER_FLAG,
    dest=_DEVICE_NAME_FILTER_FLAG,
    type=str,
    default="",
    help="Filter device name by regex.")
ap.add_argument(
    "-n",
    "--%s" % _NODE_NAME_FILTER_FLAG,
    dest=_NODE_NAME_FILTER_FLAG,
    type=str,
    default="",
    help="Filter node name by regex.")
ap.add_argument(
    "-t",
    "--%s" % _OP_TYPE_FILTER_FLAG,
    dest=_OP_TYPE_FILTER_FLAG,
    type=str,
    default="",
    help="Filter op type by regex.")
ap.add_argument(
    "--init_line",
    dest="init_line",
    type=int,
    default=0,
    help="The 1-based line number to scroll to initially.")

self._arg_parsers["print_source"] = ap
