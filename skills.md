As of 2023:

* Python - I've been developing in Python on and off for 14 years. I fixed a
  bug in the Guake Terminal for Linux while I was in high school, before I
  realized that a later release actually already fixed the bug in similar way
  to me. At UC Berkeley, I took a parsers and compilers course in Python where
  over the semester we implemented a scaled-down version of Lua and learned
  about the internals of interpreted languages like Python, and how to perform
  syntax transformations, aka "syntactic sugaring." Also during college, I took
  on a paid web project using Django+Python to implement a web server with
  login, custom handlers and other server-side logic. Soon after, I released
  intervaltree as open source, a pure Python 2&3 data structure for operations
  on collections of intervals/ranges. I also did internships which used Python
  to send newsletters to customers via email. Upon leaving the university, I
  continually encountered command line tooling, such as Google's `gcloud` and
  `gsutil` commands, and plugins for vim, which I occasionally needed to debug
  and install isolated python environments for. For the online version of my
  resume at [chaimleib.com/resume](https://chaimleib.com/resume), I used Python
  to postprocess the HTML emitted from a Markdown-to-HTML converter, in order
  to obfuscate my email and phone number from web scrapers for scam
  communications.

* API design - My first introduction to API design was at UC Berkeley. Over
  several courses, I was trained in the use of scopes to hide implementation
  details and secrets, how access levels for fields and methods work in
  Object-Oriented Programming for Java, and the advantages of pure functions,
  higher-order programming and function composition for complex projects. The
  results of this learning can be seen in my intervaltree Python library.
  Although I originally created it for tagging spans of text, my API was
  generalized enough to find use in genome research and computer vision, and
  many academic papers have been written that cite my library. Rustici Software
  had me help build
  [TinCanPython](https://github.com/RusticiSoftware/TinCanPython), a
  client-side API for logging military or work training to the cloud, as well
  as other xAPI (Experience API) projects.  My later work at Evernote to
  re-architect evernote.com was heavily influenced by my experiences, in that I
  stressed separation of concerns, single sources of truth, simplicity for
  other developers, and clear organization. All of these systems I designed and
  built have lasted for more than 6 years and are still in active use.

* Java -  I first learned Java for my Data Structures course at UC Berkeley,
  and since then have encountered it at a few different jobs. My impression of
  Java as a student and Java as working developer were quite different. In
  school the emphasis was on algorithms and computation, but at work the
  emphasis was on abstraction, indirection, and dependency inversion, primarily
  to facilitate unit testing. I encountered some industrial Java at Rustici
  Software, but more so at Evernote, where the backend monolith was mostly Java
  using Spring.

* Linux - I have over 20 years of experience with various flavors of Linux. My
  earliest was with dual-booting Puppy Linux with Mac OS 8. Throughout high
  school, I gathered discarded computer parts, installed Ubuntu on resulting
  franken-puter, and used it to test what I had learned by auditing a Computer
  Networking course at Vanderbilt University. At UC Berkeley, all of our
  technical classes required ssh to CentOS, Solaris or RedHat Linux machines,
  which was when I began committing my dotfiles to GitHub. In my personal time,
  I twice completed the Linux From Scratch project, starting with a bare hard
  drive and compiling all the components of a Linux system from source code to
  make it bootable. Once was in 2010, the next time in 2021. At work, I wrote
  shell scripts to deploy services to Linux servers, usually running either
  Ubuntu or Debian. In writing Dockerfiles, I typically target Alpine Linux
  because of the smaller image size and faster boot. When writing web servers
  to run in Google Cloud Platform, I was constantly aware that the OS I was
  running on was some type of Linux.

* Fullstack - In addition to my backend experience detailed above, I have been
  developing frontend for websites since I was 11 years old, over 20 years ago.
  I got introduced to CSS soon after it was introduced when I was still in
  middle school. I began playing with JavaScript soon after, and in college I
  got introduced to jQuery and Angular.js. In the workplace, I learned React.js
  for Coupa Software and Evernote. At Evernote, my work still lives at
  [evernote.com/careers](https://evernote.com/careers) where I used React to
  filter job descriptions, and I also made contributions to the note editing
  app using React. At first, we used FlowScript to perform typechecking on our
  JavaScript, before we migrated to TypeScript. For the re-architecting of
  evernote.com, I configured webpack from scratch, adding reactive code
  compilation for not just the frontend, but the backend as well. I developed
  and maintained several microservices as part of that project, which handled
  translations, the CMS, content updates, IP address to geographical location
  conversion, and automatic updates for app download links.
