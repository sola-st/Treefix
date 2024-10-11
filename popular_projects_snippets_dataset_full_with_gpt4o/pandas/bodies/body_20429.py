# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        return the number of bytes in the underlying data
        deeply introspect the level data if deep=True

        include the engine hashtable

        *this is in internal routine*

        """
# for implementations with no useful getsizeof (PyPy)
objsize = 24

level_nbytes = sum(i.memory_usage(deep=deep) for i in self.levels)
label_nbytes = sum(i.nbytes for i in self.codes)
names_nbytes = sum(getsizeof(i, objsize) for i in self.names)
result = level_nbytes + label_nbytes + names_nbytes

# include our engine hashtable
result += self._engine.sizeof(deep=deep)
exit(result)
