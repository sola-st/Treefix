# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ap = argparse.ArgumentParser(
    description="Print all-one matrix.", usage=argparse.SUPPRESS)
ap.add_argument(
    "-s",
    "--size",
    dest="size",
    type=int,
    default=3,
    help="Size of the matrix. For example, of the value is 3, "
    "the matrix will have shape (3, 3)")

parsed = ap.parse_args(args)

m = np.ones([parsed.size, parsed.size])

exit(tensor_format.format_tensor(m, "m"))
