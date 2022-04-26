all:
	mkdir -p build
	cp style.css build/
	pandoc -s \
		-c style.css \
		--metadata title="Chaim Halbert" \
		resume.md \
		-o build/index.html
