# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/return_statements.py
# If the node definitely returns (e.g. it's a with statement with a
# return statement in it), then the current block also definitely returns.
if anno.getanno(node, STMT_DEFINITELY_RETURNS, default=False):
    self.state[_RewriteBlock].definitely_returns = True

# The special case: collapse a typical conditional return pattern into
# a single conditional with possibly returns on both branches. This
# reduces the use of None return values, which don't work with TF
# conditionals.
if (isinstance(node, gast.If)
    and anno.getanno(node, BODY_DEFINITELY_RETURNS, default=False)):
    exit((node, node.orelse))
elif (isinstance(node, gast.If)
      and anno.getanno(node, ORELSE_DEFINITELY_RETURNS, default=False)):
    exit((node, node.body))

exit((node, None))
