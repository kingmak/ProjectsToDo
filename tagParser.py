projMap = {}
loc = 'projList'
key = ''

with open(loc) as File:
	for line in File:

		if '</' in line or line == '\n':
			pass

		elif '<' in line:
			key = line.strip()[1:-1]
			projMap[key] = []

		else:
			projMap[key].append(line.strip())

def genHtml(zeProjMap, filename):
	htmlFile = open(filename, 'w')
	htmlFile.write('<html>\n<body>\n')

	for key, value in zeProjMap.iteritems():
		htmlFile.write('\t<h2>1. %s</h2>\n\t<ol>\n' % key)
		for item in value:
			htmlFile.write('\t\t<li><a href="%s" target="_blank">%s</a></li>\n' % (item, item))
		htmlFile.write('\t</ol>\n')
	htmlFile.close()

def printMap(zeProjMap):
	for key, value in zeProjMap.iteritems():
		print key
		for item in value:
			print '   ', item
		print ''

printMap(projMap)
genHtml(projMap, 'map.html')


