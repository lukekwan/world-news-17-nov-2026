#!/usr/bin/env python3
"""Write the front-page image to /output/entry.png.

The image is a pre-rendered 1024x1024 PNG held in this repository
(entry.png). This program copies it byte-for-byte, so two runs always
produce identical output.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, "/output/entry.png")


if __name__ == "__main__":
    main()
