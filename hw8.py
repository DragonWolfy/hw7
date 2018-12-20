def get_words(filename):
    words=[]
    with open(filename, encoding='utf8') as file:
        text = file.read()
        words=text.split(' ')
    return words


def words_filter(words, an_input_command):
    if an_input_command==('min_length'):
        print('1')
        a=('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        for word in words:
            if len(word)<len(a):
                a=word
        print(len(a))
            
    elif an_input_command==('contains'):
        print('1')
        the_contained=input('What is contained? ')
        for word in words:
            for letter in word:
                if the_contained==letter:
                    print(word)
                else:
                    continue
    else:
        print('0')
        print('Can not work with', '"',an_input_command, '"')



def main():
    words = get_words('example.txt')
    a=input('input second variable: ')
    filtered_words = words_filter(words, a)



__name__=input('input command: ')
if __name__ == '__main__':
    main()
    
