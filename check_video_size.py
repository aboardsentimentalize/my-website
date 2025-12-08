#!/usr/bin/env python
"""Check video file size"""
import os

input_file = r'P:\Scripts\my-website\build\videos\Acting reel.mov'

if os.path.exists(input_file):
    size_bytes = os.path.getsize(input_file)
    size_mb = size_bytes / (1024 * 1024)
    print(f"File: {input_file}")
    print(f"Size: {size_mb:.2f} MB ({size_bytes:,} bytes)")

    if size_mb < 25:
        print(f"\nFile is already under 25MB! No compression needed.")
        print(f"You can use it as-is.")
    else:
        print(f"\nFile is {size_mb - 25:.2f} MB over the 25MB limit.")
        print(f"Compression needed.")
else:
    print(f"Error: File not found at {input_file}")
