# Extracted from https://stackoverflow.com/questions/710551/use-import-module-or-from-module-import
bar = "apples"

import foo
foo.bar = "oranges"   # update bar inside foo module object

import foo           
print foo.bar        # if executed after a's "foo.bar" assignment, will print "oranges"

from foo import bar
bar = "oranges"

