all:
	mkdir -p build
	cp style.css build/
	pandoc -s \
		-c style.css \
		--metadata title="Chaim Halbert" \
		resume.md \
		-o build/pandoc.html
	./postprocess.py build/pandoc.html -o build/index.html
	@# postprocess.py has embedded style.css into index.html, so we don't need
	@# these anymore
	rm build/pandoc.html build/style.css

clean:
	rm -rf build

.PHONY: all clean
