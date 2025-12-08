@echo off
echo Compressing Acting reel to under 25MB...
echo.

cd /d "P:\Scripts\my-website\build\videos"

P:\ffmpeg\bin\ffmpeg.exe -i "Acting reel.mov" -c:v libx264 -b:v 1200k -c:a aac -b:a 96k -movflags +faststart -y "Acting reel_compressed.mov"

echo.
echo Done! Check the file size:
dir "Acting reel_compressed.mov"
echo.
pause
