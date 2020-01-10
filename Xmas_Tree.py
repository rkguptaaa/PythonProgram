picture = [
        [0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,1,1,0,0],
        [0,1,1,1,1,1,0],
        [0,1,1,1,1,1,0],
        [1,1,1,1,1,1,1],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1]
        ]

for item in picture:
    print('')
    for pix in item:
        fill = '*'
        empty = ' '
        #if(pix == 0):
        #    print(' ')
        #else:
        #    print('1')
        #pixelLine += ' ' if pix == 0 else pixelLine += "e"
        if not pix:
            print(empty, end='')
        else:
            print(fill, end='')
    