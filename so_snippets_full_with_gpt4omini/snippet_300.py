# Extracted from https://stackoverflow.com/questions/4690600/python-exception-message-capturing
try:
    # my code
except SomeError as e:
    logger.debug(e, exc_info=True)

try:
    # my code
except SomeError as e:
    logger.exception(e)

