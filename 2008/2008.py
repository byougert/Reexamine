from re import findall


def filter_word(text: str):
    return findall('[a-zA-Z]+', text)


def main():
    with open('2008.txt', 'r', encoding='utf-8') as f, open('2008_output.txt', 'w+', encoding='utf-8') as p:
        words = filter_word(f.read())
        title_words = [word.title() for word in words if word.upper() != 'THE']
        print(title_words)

        for word in title_words:
            p.write(word + '\n')


if __name__ == '__main__':
    main()