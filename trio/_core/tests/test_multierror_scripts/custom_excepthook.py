import _common

import sys

def custom_excepthook(*args):
    print("custom running!")
    return sys.__excepthook__(*args)
sys.excepthook = custom_excepthook

# Should warn that we'll get kinda-broken tracebacks
import trio

# The custom excepthook should run, because trio was polite and didn't
# override it
raise trio.MultiError([ValueError(), KeyError()])
