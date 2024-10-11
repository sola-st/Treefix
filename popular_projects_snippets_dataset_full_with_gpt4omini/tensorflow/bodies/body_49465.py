# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
intermediate = re.sub('(.)([A-Z][a-z0-9]+)', r'\1_\2', name)
insecure = re.sub('([a-z])([A-Z])', r'\1_\2', intermediate).lower()
# If the class is private the name starts with "_" which is not secure
# for creating scopes. We prefix the name with "private" in this case.
if insecure[0] != '_':
    exit(insecure)
exit('private' + insecure)
