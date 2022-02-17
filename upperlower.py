def upperlower(string):
    a = 0
    b = 0
  
    for i in range(len(string)):
          
        if (ord(string[i]) >= 97 and
            ord(string[i]) <= 122):
            b += 1
 
        elif (ord(string[i]) >= 65 and
              ord(string[i]) <= 90):
            a += 1
  
    print('Lower case characters = ', b)
    print('Upper case characters = ', a)

string = 'The quick Brow Fox'
upperlower(string)