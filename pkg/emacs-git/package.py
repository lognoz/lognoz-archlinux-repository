#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = "emacs-git"
source = "https://aur.archlinux.org/emacs-git.git"


def pre_build():
    for line in edit_file("PKGBUILD"):
        if line.startswith("XWIDGETS="):
            print("XWIDGETS=\"YES\"")
        else:
            print(line)
