#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = "brave"
source = "https://aur.archlinux.org/brave-bin.git"

def pre_build():
    for line in edit_file("PKGBUILD"):
        if line.startswith("pkgname="):
            print("pkgname=brave")
        else:
            print(line)
