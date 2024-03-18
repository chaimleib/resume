#!/bin/bash

CHROME=
for prog in \
  /Applications/"Brave Browser.app"/Contents/MacOS/"Brave Browser" \
  /Applications/"Chromium.app"/Contents/MacOS/"Chromium" \
  "$(command -v brave-browser)" \
  "$(command -v chromium)" \
  "$(command -v chrome)" \
  ; do
  if [ -x "$prog" ]; then
    CHROME=$prog
    break
  fi
done
if [[ -z "$CHROME" ]]; then
  echo "no chrome found" >&2
  exit 1
fi
echo "found chrome: $CHROME"
exec "$CHROME" \
  --headless \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf="$2" \
  "$1"
