def get_book_text(file_path):
	with open(file_path) as f:
		file_content = f.read()
		if file_content:
			print("Read Success")


def word_count(file_path):
	with open(file_path) as f:
		file_content = f.read()
		words = file_content.split()
	word_count = len(words)
	print(f"{word_count} words found in the document")





if __name__ == "__main__":
	word_count("books/frankenstein.txt")
