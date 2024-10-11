# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/copy_binary.py
"""This script copies binaries.

  Requirements:
    filename: The path to the whl file
    AND
    new_py_ver: Create a nightly tag with current date

  Raises:
    RuntimeError: If the whl file was not found
  """

parser = argparse.ArgumentParser(description="Cherry picking automation.")

# Arg information
parser.add_argument(
    "--filename", help="path to whl file we are copying", required=True)
parser.add_argument(
    "--new_py_ver", help="two digit py version eg. 27 or 33", required=True)

args = parser.parse_args()

# Argument checking
args.filename = os.path.abspath(args.filename)
check_existence(args.filename)
regex_groups = re.search(TF_NIGHTLY_REGEX, args.filename)
directory = regex_groups.group(1)
package = regex_groups.group(2)
version = regex_groups.group(3)
origin_tag = regex_groups.group(4)
old_py_ver = re.search(r"(cp\d\d)", origin_tag).group(1)

# Create new tags
new_tag = origin_tag.replace(old_py_ver, "cp" + args.new_py_ver)

# Copy the binary with the info we have
copy_binary(directory, origin_tag, new_tag, version, package)
