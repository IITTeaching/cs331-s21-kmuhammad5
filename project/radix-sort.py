import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()
max1 = 127
def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    bookwords = book_to_words()
    maxLen = len(max(bookwords, key = len))

    #Pad the input so we don't have to worry about index out of bounds
    for i in range(len(bookwords)):
        bookwords[i] = bookwords[i].decode('ascii')
        #bookwords[i].replace('?', '')
        if len(bookwords[i]) < maxLen:
            while len(bookwords[i]) < maxLen:
                bookwords[i] = bookwords[i] + '@'
        bookwords[i] = bytes(bookwords[i], encoding='ascii')

    def lsd(arr):
      n = len(arr)
      for d in reversed(range(maxLen)):
        count = [0] * 128
        output = [''] * n
        for i in range(n):
          count[arr[i][d] + 1] += 1
        for k in range(1, 128):
          count[k] += count[k-1]
        for j in range(n):
          output[count[arr[j][d]]] = arr[j]
          count[arr[j][d]] += 1
        for m in range(n):
          arr[m] = output[m]
    lsd(bookwords)
    for i in range(len(bookwords)):
        bookwords[i] = bookwords[i].decode('ascii')
        bookwords[i] = bookwords[i].replace('@', '')
        bookwords[i] = bytes(bookwords[i], encoding='ascii')
    return bookwords

#output = radix_a_book()
#for i in range(len(output)):
    #print(output[i])
