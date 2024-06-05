def main():
	book_path = "books/frankenstein.txt"
	text = get_text(book_path)
	word_count = get_word_count(text)
	character_count = get_character_count(text)
	print(f"--- Begin report of {book_path} ---")
	print (f"{word_count} words found in the document")
	print (f"{character_count}")
	

def get_word_count(text):
	words = text.split()
	return len(words)

def get_text(path):
	with open(path) as f:
	    return f.read()

def get_character_count(text):
	lowered_text = text.lower()
	letter_dictionary = dict()
	letter_dictionary = {
	}
	letter_list = [
	]
	for letter in lowered_text:
		if letter.isalpha():
			if letter not in letter_dictionary:
				letter_dictionary[letter] = 1
			else:
				letter_dictionary[letter] += 1
	for letter, count in letter_dictionary.items():
		new_dict = {"letter": letter, "count": count}
		letter_list.append(new_dict)
	letter_list.sort(reverse=True, key=sort_on)
	return letter_list	

def sort_on (dictionary) :
	return dictionary["count"]

main()

