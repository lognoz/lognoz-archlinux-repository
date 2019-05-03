#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = "dwm"
source = "https://aur.archlinux.org/dwm-git.git"
rules = '''
static const Rule rules[] = {
    /* class      instance    title       tags mask     isfloating   monitor */
    { "Firefox",  2,          NULL,       1 << 8,       0,           -1 },
};'''

def edit_package_build():
    for line in edit_file("PKGBUILD"):
        if line.startswith("depends=("):
            print(line.replace(")", " 'adobe-source-code-pro-fonts')").replace("'st'", "'xterm'"))
        else:
            print(line)

def edit_config():
    colors = {
        "#000000": [ "selbgcolor", "selbordercolor", "normbgcolor", "normbordercolor" ],
        "#D8D8D8": [ "normfgcolor" ],
        "#FFFFFF": [ "selfgcolor" ]
    }

    for line in edit_file("config.h"):
        for color in colors:
            for key in colors[color]:
                if line.startswith("static const char " + key):
                    line = replace_ending('"', '"%s";' % color, line)

        if line.startswith("static const unsigned int borderpx"):
            print(line.replace("1", "0"))

        elif line.startswith('static const char *tags'):
            print(replace_ending("{", '{ "1", "2", "3", "4", "5" };', line))
            print(rules)

        elif line.startswith("#define SHCMD("):
            print(line.replace("/bin/sh", "/bin/xterm"))

        elif line.startswith("static const char *termcmd"):
            print(line.replace('"st"', '"xterm"'))

        elif "monospace" in line:
            print(line.replace("monospace", "Source Code Pro"))

        else:
            print(line)

def remove_rules():
    writing = True

    with open("config.h", "r") as input:
        lines = input.readlines()
        with open("config.h", "w") as output:
            for line in lines:
                if line.startswith("static const Rule rules[]"):
                    writing = False

                if writing == False:
                    if line.startswith("/*"):
                        writing = True
                    else:
                        continue

                output.write(line)

def rename_package():
    for line in edit_file("PKGBUILD"):
        if line.startswith("pkgname="):
            print("pkgname=dwm")
        else:
            print(line)

def pre_build():
    rename_package()
    remove_rules()
    edit_package_build()
    edit_config()
