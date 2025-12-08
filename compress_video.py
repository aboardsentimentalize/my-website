#!/usr/bin/env python
"""Compress video to be under 25MB"""
import os
import subprocess

# Use ffmpeg from P:\ffmpeg
ffmpeg_path = r'P:\ffmpeg\bin\ffmpeg.exe'
ffprobe_path = r'P:\ffmpeg\bin\ffprobe.exe'

input_file = r'P:\Scripts\my-website\build\videos\Acting reel.mov'
output_file = r'P:\Scripts\my-website\build\videos\Acting reel_compressed.mov'

# Get current file size
current_size = os.path.getsize(input_file)
current_size_mb = current_size / (1024 * 1024)

print(f"Current file size: {current_size_mb:.2f} MB")

# Target size is just under 25MB
target_size_mb = 24.5
target_size_bytes = int(target_size_mb * 1024 * 1024)

# Calculate video bitrate
# Get video duration first
duration_cmd = [
    ffprobe_path, '-v', 'error',
    '-show_entries', 'format=duration',
    '-of', 'default=noprint_wrappers=1:nokey=1',
    input_file
]

try:
    result = subprocess.run(duration_cmd, capture_output=True, text=True, check=True)
    duration = float(result.stdout.strip())
    print(f"Video duration: {duration:.2f} seconds")

    # Calculate bitrate (leaving room for audio)
    audio_bitrate = 128  # kbps
    target_bitrate = int((target_size_bytes * 8 / duration) / 1000) - audio_bitrate

    print(f"Target video bitrate: {target_bitrate} kbps")

    # Compress video with ffmpeg
    ffmpeg_cmd = [
        ffmpeg_path, '-i', input_file,
        '-c:v', 'libx264',
        '-b:v', f'{target_bitrate}k',
        '-c:a', 'aac',
        '-b:a', '128k',
        '-movflags', '+faststart',
        '-y',
        output_file
    ]

    print(f"\nCompressing video...")
    subprocess.run(ffmpeg_cmd, check=True)

    # Check output size
    output_size = os.path.getsize(output_file)
    output_size_mb = output_size / (1024 * 1024)

    print(f"\nCompression complete!")
    print(f"Original size: {current_size_mb:.2f} MB")
    print(f"Compressed size: {output_size_mb:.2f} MB")
    print(f"Savings: {current_size_mb - output_size_mb:.2f} MB ({(1 - output_size_mb/current_size_mb)*100:.1f}%)")
    print(f"\nOutput file: {output_file}")

except Exception as e:
    print(f"Error: {e}")
