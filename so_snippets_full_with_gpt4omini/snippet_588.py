# Extracted from https://stackoverflow.com/questions/1405913/how-do-i-determine-if-my-python-shell-is-executing-in-32bit-or-64bit
import ctypes
print ctypes.sizeof(ctypes.c_voidp)

