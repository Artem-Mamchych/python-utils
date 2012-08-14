import hashlib
import base64
import sys

def getHash(text):
    result = hashlib.md5(text).digest()
    return base64.b64encode(result, "._").replace("=", "")

if __name__ == "__main__":
    if len(sys.argv) == 2 and getHash("qwertyuiop.") == "fMvy1tEpsT2DWh0GNjRsRw" and getHash("0") == "z80ghJXVZe9m59_5.Ydk2g":
        print(getHash(sys.argv[1]))