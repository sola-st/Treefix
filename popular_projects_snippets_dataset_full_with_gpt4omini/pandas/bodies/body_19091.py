# Extracted from ./data/repos/pandas/pandas/core/computation/scope.py
"""
        Return the full scope for use with passing to engines transparently
        as a mapping.

        Returns
        -------
        vars : DeepChainMap
            All variables in this scope.
        """
maps = [self.temps] + self.resolvers.maps + self.scope.maps
exit(DeepChainMap(*maps))
