'''
Converts APE files to wav and then to wavpack lossless format.

Created on Jun 19, 2011
'''
import sys
import os
from os.path import exists

helpstring = "%s converts APE files to wavpack lossless format.\n Usage: %s file1.ape [file2.ape ...] \
N\nOptions\
\n\t-v\tPrints version info \
\n\t-h\tPrints this help message \
" % (sys.argv[0], sys.argv[0])

version = "0.0 alpha"
latestversion_url = "https://raw.github.com/TQFP64/python-utils/master/src/ape2flac.py"
versionstring = "%s version: %s  Latest version avalible at:\n %s" % (sys.argv[0], version, latestversion_url)

ape_home = ''
ape_unpack = ape_home + 'mac "%s" "%s.wav" -d'
wavpack_home = ''
wavpack_embed_cuesheet = ' -w "Cuesheet=@%s"'
wavpack_pack = wavpack_home + 'wavpack -h -m %s.wav '
wavpack_pack_and_embed_cuesheet = wavpack_pack + wavpack_embed_cuesheet

"""
1. Search cuesheet file
2. Replace FILE "$filename$.wav" WAVE >to> FILE "$filename$.wv" WAVE
3. Return name of new cuesheet or None if cuesheet not found
"""
def get_cuefile(file):
    print "get_cuefile:: Serrching cuesheet"
    return 0

def convert_file(apefile, cuefile=None):
    if apefile.endswith(".ape"):
        file = os.path.splitext(apefile)[0]
        print ape_unpack % (apefile, file + ".wav")

        if exists(file + ".cue"):
            print "CUE FOUND"
            print wavpack_pack_and_embed_cuesheet % (file, file + ".cue")
        else:
            print "CUE NOT FOUND"
            print wavpack_pack % file

    else:
        print apefile + " is not an APE file!"
    return 0

"""
Parses current option and runs its action, returns True
If argument not an option returns False 
"""
def option(option):
    if option == "-h":
        print helpstring
    elif option == "-v":
        print versionstring
    else:
        return False
    return True

def main():
    for arg in sys.argv[1:]:
        if not option(arg):
            convert_file(arg)
    return 0

if __name__ == "__main__":
    main()

#Add options for compression quality