def main():

    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    def count_words(contents):
        contents = contents.split()
        count_words = len(contents)
        return count_words

    def count_characters(contents):
        counter_dict = {}
        contents = contents.lower()
        for word in contents:
            if word.isalpha() == True:
                if word in counter_dict.keys():
                    counter_dict[word] += 1
                else:
                    counter_dict[word] = 1
        return counter_dict

    def convert_dict(dict):
        parsed_list = []
        for key, value in dict.items():
            parsed = {}
            parsed["name"] = key
            parsed["num"] = value
            parsed_list.append(parsed)
        return parsed_list

    def sort_on(list_of_dict):
        return list_of_dict["num"]

    def sort_list_of_dict(list_of_dict):
        list_of_dict.sort(reverse=True, key=sort_on)
        return list_of_dict

    def sorted_report(list_dict):
        for num in list_dict:
            print(f"The '{num['name']}' character was found {num['num']}")

    counted = count_characters(file_contents)

    opening_message = f"--- Begin report of {path_to_file} ---"
    print(opening_message)
    words = count_words(file_contents)
    count_message = f"{words} words found in the document\n"
    print(count_message)

    converted = convert_dict(counted)
    sorted_val = sort_list_of_dict(converted)
    sorted_report(sorted_val)


main()
