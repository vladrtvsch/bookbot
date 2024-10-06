def main():
	file_path = "books/frankenstein.txt"
	file_text = get_file_text(file_path)
	# print(file_text)
	# word_count = count_words(file_text)
	# print(word_count)
	dict = get_char_counts(file_text)
	# print(dict)
	list_of_dict = create_structured_dict_list(dict)
	list_of_dict.sort(reverse=True, key=sort_key)
	print_line_by_line_list(list_of_dict)


def get_file_text(file_path): 
	with open(file_path) as f:
		file_contents = f.read()	
	return file_contents

def count_words(str):
	str_to_arr = str.split()
	return len(str_to_arr)

def get_char_counts(str):
	lower_str = str.lower()
	dict = {}
	for c in lower_str:
		if c in dict:
			dict[c] += 1
		else:
			dict[c] = 1
	return dict

def create_structured_dict_list(dict):
	str_dict_elem = {}
	str_dict_list = []
	for char in dict:
		if char.isalpha():
			str_dict_elem = {"name":char, "num":dict[char]}
			str_dict_list.append(str_dict_elem)
	return str_dict_list

def sort_key(dict_elem):
	return dict_elem["num"]

def print_line_by_line_list(list_of_dict):
	for dict in list_of_dict:
		print(f"The '{dict['name']}' character was found {dict['num']} times ")


main()