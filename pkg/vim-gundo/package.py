#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

name = "vim-gundo"
source = "https://github.com/lognoz/archlinux-packages"

def pre_build():
    os.system("cp ./vim-gundo/PKGBUILD ./")

    files = os.listdir(".")
    for f in files:
        if os.path.isdir(f):
            os.system("rm -rf " + f)
        elif os.path.isfile(f) and f != "package.py" and f != "PKGBUILD":
            os.remove(f)

