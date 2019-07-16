#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = "vim-youcompleteme"
source = "https://aur.archlinux.org/vim-youcompleteme-git.git"

def pre_build():
    for line in edit_file("PKGBUILD"):
        if line.startswith("pkgname="):
            print("pkgname=vim-youcompleteme")
        else:
            print(line)
