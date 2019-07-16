#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = "siji"
source = "https://aur.archlinux.org/siji-git.git"

def pre_build():
    for line in edit_file("PKGBUILD"):
        if line.startswith("pkgname="):
            print("pkgname=siji")
        else:
            print(line)
