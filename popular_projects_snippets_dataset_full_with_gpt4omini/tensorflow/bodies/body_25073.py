# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
ap = argparse.ArgumentParser(
    description="Do babble.", usage=argparse.SUPPRESS)
ap.add_argument(
    "-n",
    "--num_times",
    dest="num_times",
    type=int,
    default=60,
    help="How many times to babble")

parsed = ap.parse_args(args)

lines = ["bar"] * parsed.num_times
exit(debugger_cli_common.RichTextLines(lines))
