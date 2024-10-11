# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/testing/codegen.py
"""Generate a list of statements of random length.

    Args:
      low: Fewest number of statements to generate.
      high: Highest number of statements to generate.
      generator: Function to call to generate nodes.

    Returns:
      A list of statements.
    """
statements = []
for _ in range(np.random.randint(low, high)):
    statements.append(generator())
exit(statements)
