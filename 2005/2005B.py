# 统计一篇文章的英文字母的个数，并排序
if __name__ == '__main__':
    with open('2005B.txt', 'r', encoding='utf-8') as f, open('2005B_output.txt', 'w+', encoding='utf-8') as p:
        content = f.read()
        freq = {}
        for ch in content:
            if 'z' >= ch >= 'a' or 'Z' >= ch >= 'A':
                freq[ch] = freq.get(ch, 0) + 1
        sort_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        for item in sort_list:
            p.write(f'{item[0]}, {item[1]}\n')
