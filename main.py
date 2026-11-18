#!/usr/bin/env python3
"""Entry point for news-image-20261117 (make.fun).

Copies the pre-drawn infographic (entry.png, in this repository) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).

Standard library only, no network, no modification of the bytes:
running it twice produces byte-identical output.
"""
import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
