def read_str(filename='2016.txt'):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        content = ' '.join(lines)
        return content


def count_word(content):
    freq_dict = {}
    content_list = content.split()
    for word in content_list:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict


def dispose(freq_dict):
    high_freq_list = {key: freq_dict[key] for key in freq_dict.keys() if freq_dict[key] > 5}
    sort_dict = sorted(high_freq_list.items(), key=lambda x: x[1], reverse=True)
    return sort_dict


def output_file(sort_dict, filename='2016_output.txt'):
    with open(filename, 'w+', encoding='utf-8') as f:
        for tup in sort_dict:
            f.write(f'{tup[0]},{tup[1]}\n')


if __name__ == '__main__':
    content = read_str()
    freq_dict = count_word(content)
    sort_dict = dispose(freq_dict)
    output_file(sort_dict)
