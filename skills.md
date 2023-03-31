As of 2023:

* Google Cloud - I have been iterating on evernote.com, a GCP project, for the
  past 6-1/2 years. Originally, the site was hosted on AWS, but within my first
  year at Evernote I led the re-architecting of its functions in Google Cloud.
  This was new technology to me at the time. But the company was shutting down
  its server facilities and transitioning its edge servers over from AWS to
  GCP, so I was riding the wave. It turned out, as usual, that I was the
  fastest learner on the team, so I became the main architect by default.

  I chose to use Google App Engine for its ability to autoscale, handle edge
  node caching, and do global load balancing. GAE's designed purpose as a web
  server service was a perfect fit to our intended use-case.

  Rather than use MySQL with its potential for schema mismatches and migration
  chain breakages, I chose to use GC Storage to reap the benefits of both a
  NoSQL database and the ability to sync files to the local filesystem for
  quick-and-dirty analysis with standard command-line tools. After all, GCS is
  internally a key-value store with the facade of a filesystem.

  For adapting the CMS (unfortunately chosen and contracted without engineering
  input) to the rest of the system, including our internal translation system,
  I used Compute Engine instances configured with shell scripts that would
  relay content changes to git repositories and GC Storage buckets. This would
  allow non-engineers to update the live server with new text or images without
  dev involvement or a code deploy.

  See also the Logging and Monitoring sections for more.

  I managed secrets using KMS, propagated events using PubSub, and
  customized Jenkins instances hosted within Kubernetes configured with
  Dockerfiles.

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
  school, I gathered discarded computer parts, installed Ubuntu on the
  resulting franken-puter, and used it to test what I had learned by auditing a
  Computer Networking course at Vanderbilt University.

  When I went to UC Berkeley, all of our technical classes required ssh to
  CentOS, Solaris or RedHat Linux machines, which was when I began committing
  my dotfiles to GitHub. In my personal time, I twice completed the Linux From
  Scratch project, starting with a bare hard drive and compiling all the
  components of a Linux system from source code to make it bootable. Once was
  in 2010, the next time in 2021.

  Professionally, I wrote shell scripts to deploy services to Linux
  servers, usually running either Ubuntu or Debian. In writing Dockerfiles, I
  typically target Alpine Linux because of the smaller image size and faster
  boot. When writing web servers to run in Google Cloud Platform, I was
  constantly aware that the OS I was running on was some type of Linux, and I
  fully utilized and extended my skills in the use of Linux command-line tools.

* Fullstack - In addition to my backend experience detailed above, I have been
  developing frontend for websites since I was 11 years old, over 20 years ago.
  I got introduced to CSS soon after it was introduced when I was still in
  middle school. I began playing with JavaScript soon after, and in college I
  got introduced to jQuery and Angular.js. In the workplace, I learned React.js
  for Coupa Software and Evernote. At Evernote, my work still lives at
  [evernote.com/careers](https://evernote.com/careers) where I used React to
  filter job descriptions, and I also made contributions to the note editing
  app using React. At first, we used FlowScript to perform typechecking on our
  JavaScript, before we migrated to TypeScript.

  For the re-architecting of evernote.com, I configured webpack from scratch,
  adding reactive code compilation for not just the frontend, but the backend
  as well. I developed and maintained several microservices as part of that
  project, which handled translations, the CMS, content updates, IP address to
  geographical location conversion, and automatic updates for app download
  links.

* Testing - I created very extensive tests for Evernote to ensure that there is
  no service disruption for evernote.com. I codified the pre-deploy checklist
  and toolchain, including an automatic check on every page to make sure the
  templates are completely filled  from our actual JSON data, and nothing
  causes a server-side error.

  For each merge request, every module in the server had unit tests, mostly
  written by me for the evernote.com project, to check all the link
  transformation functions, caching data structures, glob expression parsers,
  and all the other component parts. I made an effort to keep functions small
  and simple for testing purposes so that mocking was rarely required, but when
  it was required, I took advantage of interfaces and zero values to ensure
  good code coverage and separation of concerns. Java code was of course
  heavily tested as well, both end-to-end using Selenium, and with unit tests
  and mocks. Aside from in-house tests, all code was run through the
  appropriate linter for Go, C#, Java, JavaScript, TypeScript, bash shell, and
  SCSS.

  All of these tests ran using Jenkins, which the Engineering Services team
  taught me to configure. There was a brief period when we tried using
  TeamCity, but even though I preferred the interface and speed, there was too
  much inertia in the company, and it ended up by the wayside.

  Overall, my tests were so thorough that even though I always gave the QA team
  a list of pages changed before we ran a deploy, in the last three years it
  became very rare that they found something that my tests didn't already tell
  my team about.

  At Coupa Software, we were also very heavy on Test-Driven Development in
  Javascript and Ruby, and we used Cucumber and Turnip for the purpose. I was
  even doing TDD at UC Berkeley, although typically the professors provided the
  tests. For grading of course they  took our assignments and ran them against
  their own, more extensive tests.

  In my personal projects, I have used Travis CI, Circle CI, and GitHub Actions
  together with Dockerfiles to run continuous integration tests.

* Logging - Logs are supposed to be aids to debugging. Extra noise is a
  distraction, so I strive to minimize that, but when there is a problem, I
  make an effort to provide stack traces with files, function signatures,
  important argument values and line numbers. This makes debugging much faster
  and more pleasant, and I created an errors package in Go for the purpose.

  When running evernote.com locally, an error would print an indented chain of
  errors that told me exactly why the program failed, including the arguments
  passed to the erroring function. When in production, each error would be
  emitted in JSON format together with a trace ID, so that related log lines
  could be linked with the request that triggered the error. This was critical
  because the server was multithreaded and log lines could be interleaved with
  entries from concurrent request handlers in flight. I retained the ability to
  filter log lines by error level, similar to what I was used to in Java with
  log4j, but my log messages in Go were lean and quiet enough that I never
  found this necessary.

  Every month, we would archive logs in BigQuery, and clear out old logs when
  our budget no longer allowed us to keep them in storage. Most of our
  questions could be answered from the last two weeks of logs, and I would
  occasionally filter and plot histograms of log entries using shell scripts
  and GNUplot.

* Monitoring - At Evernote, I configured and maintained many monitoring
  systems. I used Pingdom with synthetic requests to test for uptime, Datadog
  to graph and monitor 400s, 500s and response times, and PagerDuty to draw our
  attention whenever the server appeared down. This was rare, and usually
  caused by a service provider being down, like AWS, Cloudflare, or Google
  Cloud. Once, however, there was an issue with Google PubSub exceeding the
  quota of subscriptions to a channel, causing 500s as the server failed to
  boot. I resolved the immediate issue by deleting unused subscriptions by the
  hundreds, and writing a script to do this cleanup automatically on a regular
  basis. Eventually I removed the dependency on PubSub and used polling
  instead.

* AI/Machine Learning - I have classroom experience with Prof. Andrew Ng
  writing machine learning models. I view AI/ML as a powerful, yet inexact tool
  that needs to be monitored. Irreversible action should not be taken on the
  basis of AI alone, and action should certainly not be taken automatically. I
  prefer that AI report to a human first, at least during a trial period, and
  that a developer remains in control. The dev may be able to make a code
  change to avoid the questionable situation altogether while simultaneously
  improving performance. That is usually preferable to having the AI
  continuously bleeding the budget, consuming compute cycles, and reacting to
  all the noise.

  For those situations that AI/ML is required, there still remains an element
  of unpredictableness. The initial state of a Machine Learning model is a
  random seed, and the algorithms use inexact floating-point numbers, derived
  in part from that random seed. As such, for complex models, nobody completely
  understands why a model makes each and every one of its decisions, and its
  decisions are somewhat unpredictable and unrepeatable. Only code that humans
  can verify can provide a guarantee of repeatabily. Only with source code can
  you truly know that with the same input, you will get the same result. With
  ML, one of the inputs is randomness.

  I do see a place for ML, however, especially in situations like reading
  addresses at the US Post Office. Even a human sorter makes mistakes, and if
  AI consistently makes mistakes at a smaller rate over an extended period of
  time, AI is worthwhile. This is especially so if the AI can send anything it
  is uncertain about for human evaluation, which the USPS ML model does.
