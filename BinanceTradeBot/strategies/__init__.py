import importlib
import os

def get_strategy():
    dirpath = os.path.join("BinanceTradeBot", "strategies")
    filenames = os.listdir(dirpath)
    for filename in filenames:
        if filename.endswith(".py"):
            if filename == "__init__.py":
                pass
            elif filename == "__pycache__":
                pass
            else:
                name = os.path.splitext(filename)[0]
                spec = importlib.util.spec_from_file_location(name, os.path.join(dirpath, filename))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
    return None
