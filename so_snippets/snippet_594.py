# Extracted from https://stackoverflow.com/questions/3987041/run-function-from-the-command-line
python -c 'import foo; print foo.hello()'

python -c 'from foo import *; print hello()'

python -c 'from foo import hello; print hello()'

