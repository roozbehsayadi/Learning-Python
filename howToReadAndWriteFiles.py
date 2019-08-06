fw = open('sample', 'w')
fw.write('Writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

fr = open('sample', 'r')
text = fr.read()
print(text)
fr.close()
