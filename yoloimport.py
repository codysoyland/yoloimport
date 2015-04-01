import os
import types

maybe_import = __import__

def yoloimport(name, *args, **kwargs):
    try:
        return maybe_import(name, *args, **kwargs)
    except ImportError:
        # Oops, maybe it's not installed? Let's fix that!
        os.system('pip install ' + name.split('.')[0])

        # Let's try again!
        try:
            return maybe_import(name, *args, **kwargs)
        except ImportError:
            # Silly package doesn't exist. Who needs a stupid ImportError? Let's give the caller a None!
            return None

__builtins__['__import__'] = yoloimport
