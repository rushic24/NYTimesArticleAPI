import sys

PY_VER = sys.version_info[0]

if PY_VER == 2:
    from api import search
elif PY_VER == 3:
    from .api import search
else:
    raise ImportError("Only Python versions 2.7 and 3.2+ are supported")

__version__ = "1.0.0"
__author__ = "Matt Morrison @MattDMo mattdmo@mattdmo.com"
__all__ = ["search"]
