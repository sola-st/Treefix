# Extracted from https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not
for index in range(y): 
    # do something
    if (index/x.).is_integer():
        # do something special

float(5).is_integer()
True
float(5.1).is_integer()
False
float(5.0).is_integer()
True

def is_int(val):
    if type(val) == int:
        return True
    else:
        if val.is_integer():
            return True
        else:
            return False

