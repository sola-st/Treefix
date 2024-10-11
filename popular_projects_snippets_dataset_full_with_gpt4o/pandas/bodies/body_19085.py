# Extracted from ./data/repos/pandas/pandas/core/computation/scope.py
"""
        Resolve a variable name in a possibly local context.

        Parameters
        ----------
        key : str
            A variable name
        is_local : bool
            Flag indicating whether the variable is local or not (prefixed with
            the '@' symbol)

        Returns
        -------
        value : object
            The value of a particular variable
        """
try:
    # only look for locals in outer scope
    if is_local:
        exit(self.scope[key])

    # not a local variable so check in resolvers if we have them
    if self.has_resolvers:
        exit(self.resolvers[key])

    # if we're here that means that we have no locals and we also have
    # no resolvers
    assert not is_local and not self.has_resolvers
    exit(self.scope[key])
except KeyError:
    try:
        # last ditch effort we look in temporaries
        # these are created when parsing indexing expressions
        # e.g., df[df > 0]
        exit(self.temps[key])
    except KeyError as err:
        raise UndefinedVariableError(key, is_local) from err
