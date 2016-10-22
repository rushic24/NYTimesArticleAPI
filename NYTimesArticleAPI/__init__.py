import sys

PY_VER = sys.version_info[0]

if PY_VER == 2:
    from api import *
else:
    from .api import *
