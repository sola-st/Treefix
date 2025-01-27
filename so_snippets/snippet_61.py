# Extracted from https://stackoverflow.com/questions/610883/how-do-i-check-if-an-object-has-an-attribute
try:
    getattr(someObject, 'someProperty')         
except AttributeError:
    print "Doesn't exist"
else
    print "Exists"

if hasattr(someObject, 'someProp'):
    #Access someProp/ set someProp
    pass

