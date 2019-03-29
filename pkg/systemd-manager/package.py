#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = "systemd-manager"
source = "https://aur.archlinux.org/systemd-manager-git.git"

def pre_build():
    for line in edit_file("PKGBUILD"):
        if line.startswith("pkgname="):
            print("pkgname=systemd-manager")
        else:
            print(line)
