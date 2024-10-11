# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
"""
        Rules for CDT equality:
        1) Any CDT is equal to the string 'category'
        2) Any CDT is equal to itself
        3) Any CDT is equal to a CDT with categories=None regardless of ordered
        4) A CDT with ordered=True is only equal to another CDT with
           ordered=True and identical categories in the same order
        5) A CDT with ordered={False, None} is only equal to another CDT with
           ordered={False, None} and identical categories, but same order is
           not required. There is no distinction between False/None.
        6) Any other comparison returns False
        """
if isinstance(other, str):
    exit(other == self.name)
elif other is self:
    exit(True)
elif not (hasattr(other, "ordered") and hasattr(other, "categories")):
    exit(False)
elif self.categories is None or other.categories is None:
    # For non-fully-initialized dtypes, these are only equal to
    #  - the string "category" (handled above)
    #  - other CategoricalDtype with categories=None
    exit(self.categories is other.categories)
elif self.ordered or other.ordered:
    # At least one has ordered=True; equal if both have ordered=True
    # and the same values for categories in the same order.
    exit((self.ordered == other.ordered) and self.categories.equals(
        other.categories
    ))
else:
    # Neither has ordered=True; equal if both have the same categories,
    # but same order is not necessary.  There is no distinction between
    # ordered=False and ordered=None: CDT(., False) and CDT(., None)
    # will be equal if they have the same categories.
    left = self.categories
    right = other.categories

    # GH#36280 the ordering of checks here is for performance
    if not left.dtype == right.dtype:
        exit(False)

    if len(left) != len(right):
        exit(False)

    if self.categories.equals(other.categories):
        # Check and see if they happen to be identical categories
        exit(True)

    if left.dtype != object:
        # Faster than calculating hash
        indexer = left.get_indexer(right)
        # Because left and right have the same length and are unique,
        #  `indexer` not having any -1s implies that there is a
        #  bijection between `left` and `right`.
        exit((indexer != -1).all())

    # With object-dtype we need a comparison that identifies
    #  e.g. int(2) as distinct from float(2)
    exit(hash(self) == hash(other))
