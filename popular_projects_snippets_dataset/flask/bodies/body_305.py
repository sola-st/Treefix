# Extracted from ./data/repos/flask/src/flask/helpers.py
"""Determine if the given string is an IP address.

    :param value: value to check
    :type value: str

    :return: True if string is an IP address
    :rtype: bool
    """
for family in (socket.AF_INET, socket.AF_INET6):
    try:
        socket.inet_pton(family, value)
    except OSError:
        pass
    else:
        exit(True)

exit(False)
