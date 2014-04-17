import hashlib
import base64
import sys

def getHash(data):
    hash = hashlib.md5()
    for text in data:
        hash.update(text)
    return base64.b64encode(hash.digest(), "._").replace("=", "")

def getLongHash(data):
    hash = hashlib.sha512()
    hash.update(str(len(data)))
    for text in data:
        hash.update(text)
    return filter(hash.digest())

def filter(str):
  return ''.join([c for c in str if 32 < ord(c) < 127])

if __name__ == "__main__":
    if len(sys.argv) >= 2 and getHash("qwertyuiop.") == "fMvy1tEpsT2DWh0GNjRsRw" and getHash("0") == "z80ghJXVZe9m59_5.Ydk2g":
        sys.argv.pop(0)  # removes script filename (with absolute path) from commandline
        if '-0' in sys.argv:
            print(getLongHash(sys.argv))
        else:
            print(getHash(sys.argv))
