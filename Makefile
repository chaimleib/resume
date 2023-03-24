all:
	mkdir -p build
	cp style.css build/
	pandoc -s \
		-c style.css \
		--metadata title="Chaim Halbert" \
		resume.md \
		-o build/pandoc.html
	./postprocess.py build/pandoc.html -o build/index.html
	rm build/pandoc.html

clean:
	rm -rf build

.PHONY: all clean
