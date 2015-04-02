import os

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
            # dang
            if name == "mock":
                return None
            else:
                # we couldn't install the package - let's return a
                # mock object - they're pretty useful!
                mock = yoloimport("mock")
                if mock is not None:
                    return mock.MagicMock()


__builtins__['__import__'] = yoloimport
