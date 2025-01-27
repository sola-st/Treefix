# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ap = argparse.ArgumentParser(
    description="Do babble.", usage=argparse.SUPPRESS)
ap.add_argument(
    "-n",
    "--num_times",
    dest="num_times",
    type=int,
    default=60,
    help="How many times to babble")
ap.add_argument(
    "-l",
    "--line",
    dest="line",
    type=str,
    default="bar",
    help="The content of each line")
ap.add_argument(
    "-k",
    "--link",
    dest="link",
    action="store_true",
    help="Create a command link on each line")
ap.add_argument(
    "-m",
    "--menu",
    dest="menu",
    action="store_true",
    help="Create a menu for testing")

parsed = ap.parse_args(args)

lines = [parsed.line] * parsed.num_times
font_attr_segs = {}
if parsed.link:
    for i in range(len(lines)):
        font_attr_segs[i] = [(
            0,
            len(lines[i]),
            debugger_cli_common.MenuItem("", "babble"),)]

annotations = {}
if parsed.menu:
    menu = debugger_cli_common.Menu()
    menu.append(
        debugger_cli_common.MenuItem("babble again", "babble"))
    menu.append(
        debugger_cli_common.MenuItem("ahoy", "ahoy", enabled=False))
    annotations[debugger_cli_common.MAIN_MENU_KEY] = menu

output = debugger_cli_common.RichTextLines(
    lines, font_attr_segs=font_attr_segs, annotations=annotations)
exit(output)
