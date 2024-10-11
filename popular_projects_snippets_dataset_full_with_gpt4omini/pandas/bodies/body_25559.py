# Extracted from ./data/repos/pandas/pandas/util/_print_versions.py
from optparse import OptionParser

parser = OptionParser()
parser.add_option(
    "-j",
    "--json",
    metavar="FILE",
    nargs=1,
    help="Save output as JSON into file, pass in '-' to output to stdout",
)

(options, args) = parser.parse_args()

if options.json == "-":
    options.json = True

show_versions(as_json=options.json)

exit(0)
