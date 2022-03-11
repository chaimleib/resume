all:
	pandoc -s \
		-c resume.css \
		--metadata title="Chaim Raymond Halbert" \
		resume.md \
		-o resume.html
