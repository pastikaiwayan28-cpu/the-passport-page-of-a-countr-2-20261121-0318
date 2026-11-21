#!/usr/bin/env python3
"""Entry program for make.fun bounty the-passport-page-of-a-countr-2-20261121-0318.

The repository holds entry.png next to this file; the program validates it
(PNG signature, IHDR 1024x1024, size at most 1 MiB, CRC32 of every chunk,
a complete IEND chunk and nothing trailing) and copies it byte for byte to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png when set), then verifies
the copy by SHA-256. Standard library only, no network, deterministic:
two runs write identical bytes.
"""
import hashlib
import os
import struct
import sys
import zlib

MAX_BYTES = 1_048_576
WANT_W, WANT_H = 1024, 1024
PNG_SIG = b"\x89PNG\r\n\x1a\n"


def fail(msg):
    print("main.py: " + msg, file=sys.stderr)
    sys.exit(1)


def read_png(path):
    try:
        with open(path, "rb") as fh:
            data = fh.read()
    except OSError as exc:
        fail("cannot read %s: %s" % (path, exc))
    if len(data) > MAX_BYTES:
        fail("entry.png is %d bytes, over the 1 MiB limit" % len(data))
    if data[:8] != PNG_SIG:
        fail("entry.png does not start with the PNG signature")
    pos = 8
    seen_ihdr = False
    seen_iend = False
    while pos < len(data):
        if pos + 8 > len(data):
            fail("truncated chunk header at offset %d" % pos)
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        ctype = data[pos + 4:pos + 8]
        end = pos + 8 + length + 4
        if end > len(data):
            fail("truncated %r chunk at offset %d" % (ctype, pos))
        body = data[pos + 8:pos + 8 + length]
        (want_crc,) = struct.unpack(">I", data[pos + 8 + length:end])
        if zlib.crc32(ctype + body) & 0xFFFFFFFF != want_crc:
            fail("bad CRC32 in %r chunk" % ctype)
        if ctype == b"IHDR":
            if length != 13:
                fail("IHDR is %d bytes, expected 13" % length)
            w, h = struct.unpack(">II", body[:8])
            if (w, h) != (WANT_W, WANT_H):
                fail("IHDR is %dx%d, expected 1024x1024" % (w, h))
            seen_ihdr = True
        if ctype == b"IEND":
            if length != 0:
                fail("IEND carries %d bytes" % length)
            seen_iend = True
            if end != len(data):
                fail("%d trailing bytes after IEND" % (len(data) - end))
            break
        pos = end
    if not seen_ihdr:
        fail("no IHDR chunk")
    if not seen_iend:
        fail("no IEND chunk")
    return data


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    data = read_png(src)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as fh:
        fh.write(data)
    with open(dst, "rb") as fh:
        copied = fh.read()
    if hashlib.sha256(copied).hexdigest() != hashlib.sha256(data).hexdigest():
        fail("SHA-256 mismatch after copy")
    print("wrote %s (%d bytes, sha256 %s)"
          % (dst, len(copied), hashlib.sha256(copied).hexdigest()))


if __name__ == "__main__":
    main()
