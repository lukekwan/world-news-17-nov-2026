#!/usr/bin/env python3
"""Write the front-page image to /output/entry.png.

The image is a pre-rendered 1024x1024 PNG held in this repository
(entry.png). This program copies it byte-for-byte, so two runs always
produce identical output. After copying it verifies the output: the
file must start with the PNG signature, must be at most 1 MiB, and must
be byte-identical to the source. Any failed check exits non-zero.

Note: the image itself is a fixed asset — the program never edits it,
it only delivers it and proves the delivery is intact.
"""
import os
import shutil
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1 * 1024 * 1024
OUTPUT_PATH = "/output/entry.png"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    dst = OUTPUT_PATH
    shutil.copyfile(src, dst)

    with open(dst, "rb") as f:
        data = f.read()
    if data[:8] != PNG_SIGNATURE:
        fail("output is not a PNG file")
    if len(data) > MAX_BYTES:
        fail(f"output is {len(data)} bytes, over the 1 MiB limit")
    with open(src, "rb") as f:
        original = f.read()
    if data != original:
        fail("output differs from entry.png")

    print(f"wrote {dst} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
