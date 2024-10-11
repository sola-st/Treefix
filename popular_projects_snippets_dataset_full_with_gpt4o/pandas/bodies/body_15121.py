# Extracted from ./data/repos/pandas/pandas/tests/base/test_constructors.py
# these show that in order for the delegation to work
# the _delegate_* methods need to be overridden to not raise
# a TypeError

self.Delegate._add_delegate_accessors(
    delegate=self.Delegator,
    accessors=self.Delegator._properties,
    typ="property",
)
self.Delegate._add_delegate_accessors(
    delegate=self.Delegator, accessors=self.Delegator._methods, typ="method"
)

delegate = self.Delegate(self.Delegator())

msg = "You cannot access the property prop"
with pytest.raises(TypeError, match=msg):
    delegate.prop

msg = "The property prop cannot be set"
with pytest.raises(TypeError, match=msg):
    delegate.prop = 5

msg = "You cannot access the property prop"
with pytest.raises(TypeError, match=msg):
    delegate.prop
