# resume

Data and scripts to generate my resume as HTML and PDF.

# Building

You will need the following:

* Python 3.6+
* pandoc
* GNU make

1. Run `make`. This will generate `build/index.html`, with embedded CSS.
1. Open `build/index.html` in a Chromium-based browser.
1. Print to PDF, and save the result to `resume.pdf`.
1. Copy `build/index.html` to the `chaimleib.github.io` repo, to `_layouts/resume.html`. This assumes I am still using GitHub Pages with jekyll.

