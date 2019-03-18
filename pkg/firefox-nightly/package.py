#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = "firefox-nightly"
source = "https://aur.archlinux.org/firefox-nightly.git"

def pre_build():
    for line in edit_file("PKGBUILD"):
        if line.strip().startswith("echo \"${_version}."):
            print("  echo \"${_version}.$(date +%Y%m)\"")
        else:
            print(line)
