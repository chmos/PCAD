#! /usr/bin/env python3

import os
import sys
import shutil
import re

def get_env(text:str)->str:
    """get the environmental variable from a string.
    An env variable begings with $ and followed by letter, _ 
    or digit 
    """
     # Define the regex pattern
    pattern = "\$[a-zA-Z]+[a-zA-Z0-9_]*"
    
    # Use re.findall to extract all matches
    matches = re.findall(pattern, text)
    return matches

def replace_env(v:str, alterValue = None) -> str:
    """replace the environment variables by their values
    if alterValue is not None, simply replace them by
    alterValue. This is because we want to change their
    original behavior
    """
    m = get_env(v)
    if m:
        for a in m:
            if alterValue is None:
                b = os.getenv(a[1:]) # remove $
                if not b:
                    b = ""
            else:
                b = alterValue
            v = v.replace(a, b)
    return v

    
def main(file, alterFolder = None):
    """ Open the DRC file and fetch all the includes 
    """
    text = open(file).read()
    lst = text.split("\n")

    # "Include $PEGASUS_DRC/Include/*.drc.pvl"
    TAG = "Include"
    for s in lst:
        s = s.strip()
        if not s.startswith(TAG):
            continue
        a = s[len(TAG):].strip()

        # replace environemental variables
        src = replace_env(a)

        # copy this file to this dir
        dst = replace_env(a, alterValue = alterFolder)

        # make sure the folder exists
        fd = os.path.dirname(dst)
        if not os.path.exists(fd):
            os.makedirs(fd, exist_ok = True)

        shutil.copy2(src, dst)
        print("copy", src, "->", dst)


if __name__ == "__main__":
    # m = replace_env(sys.argv[1], alterValue =  "./")
    # print(m)
    if len(sys.argv) < 3:
        print("Usage: fecth.py <drc_file> [dst_folder]")
        exit(0)

    main(sys.argv[1], sys.argv[2])
