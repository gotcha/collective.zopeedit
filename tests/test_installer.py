import os.path
import os

def test():
    path = list()
    path.append("C:")
    path.append("Program Files (x86)")
    path.append("ZopeExternalEditor")
    path.append("zopeedit.exe")
    assert os.path.exists(os.sep.join(path))
