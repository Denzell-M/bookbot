def get_file_content(file_path):
	with open(file_path) as f:
		file_content = f.read()
		return file_content


def word_count(file_path):
	words = get_file_content(file_path).split()
	word_count = len(words)
	print(f"{word_count} words found in the document")

