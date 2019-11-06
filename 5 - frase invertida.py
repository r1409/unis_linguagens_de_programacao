def invertida(frase):
     invert = frase.split()
for i in xrange(len(invert)):
    invert[i] = invert[i][::-1]
    return '  '.join(invert)


frase = 'Viva o mundo da tecnologia'
print
fraseInvert(invertida)
