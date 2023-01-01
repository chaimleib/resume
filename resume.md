<div id="bsd" dir="rtl">בס״ד</div>
#### Phoenix, AZ 85016
#### github.com/chaimleib — chaim.leib.halbert@gmail.com

## Goals
* Innovative backend/full-stack engineering or hardware design employment
* Remote or in Phoenix area
* Produce and iterate on a product demonstrating concrete consumer value, e.g. an app, website, appliance or device
* Protect privacy, empower the customer

## Skills

**Coding**: &gt;50 programming languages for different purposes, cross-pollinates concepts between them, constantly learning more (currently Bison). Expert and actively working in Go, C#, JS/Node.js, bash and zsh shell, and awk. Recent work and personal project experience in Java, TypeScript, Python, Ruby, and C. Designs recursively-linked data structures and algorithms. Has written multithreaded, asynchronous and concurrent code in Go, Python, JS, C, Java and bash shell. Intimately familiar with git internals. Uses tmux and vim daily, and familiar with several IDEs, including Visual Studio Code, IntelliJ (and family), Xcode, and Eclipse.

**Development process engineering**: Designs customized systems and operating procedures for the problem and the team, some of which have been battle-tested for six years and are still going strong.

**Security and privacy**: Catches potential attack vectors at code review. Protects coworkers' and customers' privacy as a matter of deep personal conviction to "do no harm," while allowing the power and flexibility to get the job done.

**Web technologies**: Experienced in Go, Node.js, React, SCSS, Webpack, Ruby on Rails, and Django for full stack web development.

**Electronics**: Designed with industrial PLCs, Arduino, Raspberry Pi, and TI microcontrollers. Designed and built analog (audio-frequency) and digital circuit boards. Implemented custom processors in Verilog for Xilinx FPGAs.

**Other**: Has studied and implemented algorithms for music synthesis and analysis, robot control, machine learning, OCR, pathfinding, 3D graphics and raytracing, parsers, compilers, interpreters, and operating systems.

## Work experience
### **Web Software Engineer and Microservices Architect, Evernote** (2016-present)

**Team process engineering**: How can I make our work easy and fun? What will likely become a bottleneck? Is training/tooling/re-architecting the best way to solve this?

**Re-architected and migrated evernote.com from PHP with AWS to Go with Google App Engine** over 6 months: It has lasted for six years and is still going strong (four previous attempts by other devs lived on average 18 months each).

* Designed and implemented HTML template system and compatibility checkers to ensure that all JSON data remains valid even as templates change.
* Codeless (and engineer-less) content updates via Crownpeak CMS (C#, command-line SSH/SFTP, Google Cloud Compute+Storage).
  * Created command-line tool in Go (Mac/Linux) to modify and query pages and C# sources on the CMS
  * Designed and built microservice to automate updates from translation service in 26 languages
  * Adapter microservices to take SFTP from CMS and mirror changes to git and Google Cloud Storage
  * Automatic Slack notifications for file changes (Google Cloud Storage, Google Cloud Pub/Sub, Google Key Management Service, Go, Slack API)
* New tooling for deploy, preview, unit test, and code quality (Go, yarn, webpack, nvm/fnm, bash/zsh, rsync, node-sass/Dart SASS, prettier, eslint, goimports, golint-ci).
* Created chainable command-line search tools in bash shell script to list assets related by (e.g.) shared JS sources, HTML template files, URLs, etc. It answers frequent questions like "Which pages use this HTML component?" or the inverse; or "Which translation languages are available for this URL?" etc. (bash, awk, grep, sed, jq/yq, xargs, etc.)
* Implemented caching and exponential backoff and retry for server-side requests in Go.
* GeoIP lookups (e.g. for country-specific sales events), automatically updated weekly (Jenkins, Go, MaxMindDB, Google Cloud Pub/Sub)
* Configured site health monitoring and reliability engineering (Google StackDriver logs, Google BigQuery logging, Pingdom, DataDog and PagerDuty)
* Analytics (Google Analytics: Commerce, Google BigQuery)

**Content Delivery Network (CDN)**: created from scratch using Google Cloud Storage. For images in Iterable promo email campaigns.

**Browser-based note editor and checkout flow**: Typescript+React frontend and Java backend.

**Jenkins continuous integration testing (BitBucket-Jenkins integration)**: No code changes are allowed into the master git branch unless the test suite passes.

**Google Cloud Platform**: scaling, hosting, Pub/Sub, BigQuery, storage, secrets management.

**Analytics and site experiments**: Used Google Analytics, Google Tag Manager, and Optimizely experiments platform with suspicion.

**Communication**: Slack (+ API), Atlassian JIRA and Confluence, BitBucket, DataDog, PagerDuty.

### **Software Engineer, Coupa Software** (2015 – 2016)

Ruby on Rails, Bootstrap, Turnip unit tests, Jenkins, and bash. Optimized RSpec test harness to work 30% faster; developed in-browser integration tests and unit tests; cooperated via AGILE with hundreds of developers using GitHub and Atlassian JIRA.

### **Software Engineer Intern, Rustici Software** (2014)

Created Python client library for TinCan API (xAPI 2.0) and created a JSON object verifier and recognizer using JSON Schema and Node.js/JavaScript. Worked on five-person team using GitHub.

### **Industrial Controls Engineer, Bridgestone** (2012)

Designed industrial controls and safety systems with AutoCAD Electrical, CoDeSys, and RSLogix. Coded PLCs in structured text (IEC 61131-3) and ladder logic, and created AutoCAD plugins with C#, Visual Basic, and LISP.

### **Computer Programmer Intern, Oak Ridge National Laboratory Physics Division** (2010)

Developed a cross-browser AJAX-based experiment log system; customized open-source software. Used PHP, JavaScript, MySQL, TinyMCE, ssh, vim, Red Hat Linux.

## Notable personal and school projects
**Completed Linux From Scratch** in 2006 and 2021 (https://www.linuxfromscratch.org/lfs/). Compiled and configured a complete Linux system from C/C++ source code and the command line.

**chaimleib.com personal website and JS audio player (zichronos)**, 2014 onward. TLS certificate/HTTPS. Static pages and media generated using Ruby, Bash and SCSS, audio player using JS+jQuery, images with Inkscape.

**github.com/chaimleib/intervaltree**, 2014 onward. Modify and query intervals in logarithmic time in pure Python 2/3. This is currently the industry reference implementation of interval trees in Python, cited in numerous academic research papers for gene research and computer vision applications, etc.

**USB Nintendo 64 Cartridge reader**, 2014. Allows backups of N64 games to the computer. Written in C for Atmega32u4 microcontroller (Teensy 1.0).

**2-axis gimballed spotlight with IR camera target tracker**, UC Berkeley EECS 149 Intro to Embedded Systems, 2014. Python, finite state machine program architecture, Raspberry Pi, Bluetooth, Nintendo Wii controller, RS485 serial servos.

**Handwritten digit recognizer**, Coursera.com Machine Learning, August 2012 with Prof. Andrew Ng. Written in Octave, an open-source clone of Matlab.

**Lua-like interpreter, parser generator and bytecode compiler**, UC Berkeley CS 164 Compilers, 2010. Written in Python 2. Also created a Vim syntax highlighting file for the new language.

## Education
### **University of California, Berkeley – College of Engineering** (2008-2014)

Studied Electrical Engineering and Computer Science. Courses covered AI, computer graphics, compilers, embedded systems, and DSP. Assignments were completed in Python, C, C++, Java, JavaScript, Matlab, Scheme, and Latex. Nearly all technical courses required ssh to bash shell on Solaris or CentOS, GNU Makefile, and some sort of VCS, usually git.

## Extended details
**Scripting languages**: JavaScript/Node.js, Typescript, Ruby, Python, Matlab, Octave, TI Basic, Lua, CoffeeScript, AppleScript

**Compiled languages**: C, C#, C++, Java, Objective-C 1.0, Objective-C 2.0, Swift, Visual Basic

**Functional programming languages**: Common LISP, AutoCAD LISP, Scheme, Racket Scheme, Haskell

**Graphical programming languages**: LabView, Max MSP, Automator, Logisim

**Shell languages**: bash, zsh, dash, tcsh, Windows BAT

**Tool languages**: GNU Makefile, Docker, BC, YACC, Bison, vimscript, awk, Regular expressions, sed, jq, yq

**Assembly and machine language architectures**: MIPS, ARM, AVR, Z80, 6502

**Databases**: PostgreSQL, MySQL, MongoDB, Redis

**Test languages**: Turnip, Cucumber, RSpec

**Hardware description languages**: Verilog and System Verilog, VHDL

**Industrial languages**: Structured text (IEC 61131-3), ladder logic, function block

**Markup languages**: Go template, ERB, HAML, Markdown, HTML, HTML5, CSS, Lilypond, LaTeX, Tikz, OpenXML

**Data storage and transmission languages**: JSON, YAML, XML, Protobuf, GNU config, Plist

**Libraries**: React, JQuery, Angular, Bootstrap, Selenium web driver, TinyMCE, Cocoa, Quartz, OpenGL, Core Foundation, Core Graphics, Jenkins, Solano, BeautifulSoup, LibXML, OpenMP, SDL, tv4 JSON validator, DatabaseCleaner, LUFA, Arduino

**Operating systems**: macOS X, Windows, Linux, Cygwin, CentOS, Arch, Manjaro, Ubuntu, Debian, Fedora, Red Hat Linux, Linux Mint, Slackware, LFS Linux From Scratch, OpenWRT, DD-WRT, Embedded Linux, RTOS

**Keywords**: responsive design, dynamic web design, unit tests, integration tests, embedded systems, AJAX, robotics, data structures, music, AI artificial intelligence, FPGA, CPLD, PCB, circuit board, microcontroller, soft processor, dotfiles, multilayer PCB layout, low-noise, Bluetooth, soldering, rework, desoldering, reflow, oscilloscope, waveform generator, IR, WiiMote, head tracking, FSM finite state machine, FSA finite state automaton, parallel processing, pipelining, real time operating system

**Can speak**: English, German, Hebrew, Yiddish, Japanese

**Can read**: English, German, Hebrew, Yiddish, Aramaic, some Japanese

**Can write**: English, German, Hebrew, Yiddish
