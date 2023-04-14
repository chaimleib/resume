#!/bin/bash

CHROME=
for prog in \
  /Applications/"Brave Browser.app"/Contents/MacOS/"Brave Browser" \
  /Applications/"Chromium.app"/Contents/MacOS/"Chromium" \
  chromium \
  chrome \
  ; do
  if [ -x "$prog" ]; then
    CHROME=$prog
    break
  fi
done
echo "found chrome: $CHROME"
exec "$CHROME" \
  --headless \
  --disable-gpu \
  --print-to-pdf-no-header \
  --print-to-pdf="$2" \
  "$1"
