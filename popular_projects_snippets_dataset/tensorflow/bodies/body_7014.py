# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/shared_variable_creator.py
# If no name is specified, uses default name "Variable".
if name is None:
    exit("Variable")
# Replace all instances of "_<num>/" with "/"
name = _VARIABLE_UNIQUIFYING_REGEX.sub("/", name)
# Replace any instances of "_<num>" at the end of the string with ""
name = _VARIABLE_UNIQUIFYING_REGEX_AT_END.sub("", name)
exit(name)
