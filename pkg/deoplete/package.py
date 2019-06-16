#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = "deoplete"
source = "https://aur.archlinux.org/deoplete-git.git"

def pre_build():
    for line in edit_file("PKGBUILD"):
        if line.startswith("pkgname="):
            print("pkgname=deoplete")
        else:
            print(line)
