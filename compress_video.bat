@echo off
echo Compressing Acting reel.mov to under 25MB...
echo.

set FFMPEG=P:\ffmpeg\bin\ffmpeg.exe
set INPUT=P:\Scripts\my-website\build\videos\Acting reel.mov
set OUTPUT=P:\Scripts\my-website\build\videos\Acting reel_compressed.mov

REM Compress with target bitrate for 24.5MB file
"%FFMPEG%" -i "%INPUT%" -c:v libx264 -b:v 1500k -c:a aac -b:a 128k -movflags +faststart -y "%OUTPUT%"

echo.
echo Compression complete!
echo Output: %OUTPUT%
echo.
pause
