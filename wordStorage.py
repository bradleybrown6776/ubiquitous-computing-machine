def storageList() :
    list = []
    new = True

  #  while 1 == 1 :
    while new == True :

        word = input('enter in the word')

        if word not in list :
            list.append(word)
            print('It\'s a new word')
            print('so far - ', list)

        elif  word in list :
            print('word is already in the list')
            print('test')


storageList()