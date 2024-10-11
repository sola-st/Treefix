# Extracted from https://stackoverflow.com/questions/338768/python-error-importerror-no-module-named
export PYTHONPATH=$PYTHONPATH:`pwd`  (OR your project root directory)

import sys
sys.path.insert(0,'<project directory>') OR
sys.path.append('<project directory>')

