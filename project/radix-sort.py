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
    listidx=0

    #Sanity Checker 1
    print(bookwords[0])
    print(bookwords[1])
    print(bookwords[2])

    #Pad the input so we don't have to worry about index out of bounds
    for i in range(len(bookwords)):
        bookwords[i] = bookwords[i].decode('ascii')
        #bookwords[i].replace('?', '')
        if len(bookwords[i]) < maxLen:
            while len(bookwords[i]) < maxLen:
                bookwords[i] = bookwords[i] + '@'
        bookwords[i] = bytes(bookwords[i], encoding='ascii')

    #Sanity Checker 2
    print(bookwords[0])
    print(bookwords[1])
    print(bookwords[2])
    print(len(bookwords))

    #Sanity Checker 3
    #print(bookwords)
    #radix(bookwords)
    instr = []

    defining = True


    def msd(arr, lowidx, highidx, d):
        if highidx <= lowidx + 1:
            return
        count = [0] * 128
        output = [''] * len(arr)
        for i in range(len(arr)):
            count[arr[i][d] + 1] += 1
        for i in range(1, 128):
            count[i] += count[i-1]
        print(count)
        for i in range(len(arr)):
            output[count[arr[i][d]]] = arr[i]
            count[arr[i][d]] += 1
        for i in range(len(arr)):
            arr[i] = output[i]

        #PseudoRecursion
        for i in range(127):
            x=d
            if (count[i+1] + 1) <= (count[i] + 2):
                while (count[i+1] + 1) <= (count[i] + 2):
                    count = [0] * 128
                    output = [''] * len(arr)
                    for j in range(len(arr)):
                        count[arr[j][x+1] + 1] += 1
                    for j in range(1, 128):
                        count[j] += count[j - 1]
                    #print(count)
                    for j in range(len(arr)):
                        output[count[arr[j][x+1]]] = arr[j]
                        count[arr[j][x+1]] += 1
                    for j in range(len(arr)):
                        arr[j] = output[j]
                    if (count[i+1] + 1) <= (count[i] + 2):
                        instr.append([count[i]+1, count[i+1] + 1, x+2])
                        x += 1
                    else:
                        break
    msd(bookwords, 0, len(bookwords), 0)
    for i in instr:
        msd(bookwords, i[0], i[1], i[2])
    return bookwords
    """for i in range(127):
            temp = instr.pop()
            print(temp)
            if temp[1] <= temp[0] + 1:
                continue
            else:
                instr.append([count[i] + 1, count[i+1] + 1, d+1])
        while len(instr) > 0:
            temp = instr.pop()
            print(temp)
            count = [0] * 128
            output = [''] * len(arr)
            for i in range(len(arr)):
                count[arr[i][temp[2]] + 1] += 1
            for i in range(1, 128):
                count[i] += count[i - 1]
            print(count)
            for i in range(len(arr)):
                output[count[arr[i][temp[2]]]] = arr[i]
                count[arr[i][temp[2]]] += 1
            for i in range(len(arr)):
                arr[i] = output[i]
            #if defining:
                #if ((count[i]+1) <= (count[i+1] + 1)):
                    #d = 0
                    #instr.append([count[i] + 1, count[i+1] + 1, d+1])
                #else:
                    #instr.append([count[i] + 1, count[i+1] + 1, d+1])

    msd(bookwords, 0, len(bookwords), 0)
    #defining = False
    for i in range(127):
        temp = instr.pop()
        print(temp)
        if temp[1] <= temp[0] + 1:
            continue
        else:
            msd(bookwords, temp[0], temp[1], temp[2])
    #msd(bookwords, 0, len(bookwords), 0)
    return bookwords

    return bookwords




    radixSort(bookwords, 0, 0, len(bookwords)-1)
    listidx = 0
    firstidx = 0
    lastidx = -1
    searching = True

    for i in range(max1):
        firstidx = lastidx
        while bookwords[lastidx][listidx] == i:
            lastidx += 1
        print(lastidx)
        if lastidx != firstidx:
            while maxLen -1 > listidx: #while there are still still strings to sort
                print(listidx)
                radixSort(bookwords, listidx + 1, firstidx, lastidx) #this wont work since the first and last idx dont change
                listidx += 1
            lastidx += 1
    #Final Sorting
    for i in range(max1):  # For each bucket
        subarr = []
        while bookwords[firstidx][listidx] == i and searching:
            subarr.append(bookwords[firstidx])
            firstidx += 1
            if firstidx > len(bookwords) - 1:
                firstidx = len(bookwords) - 1
                searching = False
        lastidx = firstidx - 1 #the last index of the bucket is the last value firstidx was updated to
        for j in range(len(bookwords)):  # for each word
            print(bookwords[j][listidx])
            print(i)
            print(j)
            if bookwords[j][listidx] == i:  # if the current "letter column"  has the value corresponding to that bucket
                subarr.append(bookwords[j])  # append that word to this list
                lastidx = j #keep track of the last index added so that the elements can be added back
            else: # if not
                continue # None of the subsequent entries will begin with that letter
        print(subarr)
        if len(subarr) > 0: #if there are values that begin with that letter
            while len(max(subarr, key=len))-1 > listidx: #while there are still strings to be sorted
                print(listidx)
                radixSort(subarr, listidx + 1) #sort those values by the next letter (and keep doing this until they are all sorted)
                listidx += 1
            for j in reversed(range(len(subarr))):
                bookwords[lastidx] = subarr[j] #adding the sorted elements back in reverse order
                lastidx -=1"""
    #return bookwords







def countingSort(arr, exp1, letteridx, beginidx, endidx):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i][letteridx] / exp1)
        count[int(index % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i][letteridx] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(beginidx, endidx + 1):
        arr[i] = output[i]


# Method to do Radix Sort

def radixSort(arr, listidx, beginidx, endidx):
    # Find the maximum number to know number of digits


    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp, listidx, beginidx, endidx)
        exp *= 10





# Driver code
# arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Function Call



# 14 is length of longest word





#Find the word with the max length in each bucket
#Do radix sort on each of the buckets
#Or, while there is a word that is longer than the counter (which tracks how far each bucket has been sorted),
#do radix sort on each bucket


#bookwords = book_to_words()

#print(len(max(bookwords, key = len)))
# radixSort(bookwords)

output = radix_a_book()
for i in range(50):
    print(output[i])
