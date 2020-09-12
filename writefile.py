#open the file 'test.txt' in the 'write' mode
#1. if the file does not exist, Python will create it
#2. if the file already exist, Python will overwrite it

filepointer = open('test.txt','w')
filepointer.write('Third Line\n')
filepointer.write('Fourth Line\n')
filepointer.write('Fifith Line\n')
filepointer.close()