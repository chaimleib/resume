My most recent job was architecting microservices. Systems that I have designed
remain popular and in-use today, some more than a decade after I first
published them as open-source.

I have an eye for creating valuable systems that other engineers love to use.
Will you let me do the same for you?

## Circuits and managing complexity
Being trained as an Electrical Engineer/CS major, I have an additional
perspective on code that lets me see it like a circuit diagram. What I mean by
that is, like a circuit, code can be split into abstract sections and analyzed
the same way, even in the middle of a function: What controls this block of
code, and how do we get the result? Also, in a massively parallel processing
chip like an FPGA, everything is literally happening at once, which is often
the case with goroutines and channels; I have mental models for synchronizing
simultaneous processes that I share between the circuit and code parts of my
brain. The computations slot in parallel streams in my mental pipeline diagram.

My code style has changed over my career. At the beginning, I strove to push
the boundaries of what languages could do. I tried to use the most powerful,
dynamic constructs available in scripted languages like Python and Ruby, in
order to understand the languages fully and be as expressive as possible. Then
I adjusted course slightly to write code as idiomatically as possible, so that
other devs could recognize my patterns and understand them quickly;
expressiveness gets complicated! Now, for the past half-decade I have been
refining my code to be as simple, readable and maintainable as I can. I have
designed APIs before and naming is important for clarity. I think a lot about
what my team will notice as I code, and I try to keep things visually simple
enough and line lengths short so that modifications and fixes are obvious. I
still have to make compromises with some libraries like GORM, but these are my
ideals.

Having reached this point, simplicity is one of the things I appreciate about
Go. Compared to Java or C++, the syntax is simpler to interpret, and the error
handling idioms are simply if-statements. That also has a beneficial effect on
the culture of Go programmers, who try to avoid hard developer dependencies on
external tooling to manage the code; "go build ." is usually enough. While the
reflect package exists for dynamic typing and annotations, its use is
discouraged due to the lower performance and typical complexity and fragility
of the result.
