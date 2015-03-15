import re

link = re.compile( "(\[.*\])(\()(.*)(\))")
url = re.compile("http.*", re.I)


def replace_links(input):
	link, _, target, __ =  input.groups()
	if not url.search(target) or target.endswith(".md"):
		target +='.md'		
	return link + "(" + target + ")"
	

def fix_links(filename):
	output = ''
	with open(filename, 'rt') as input:
		 output = re.sub(link, replace_links, input.read())

	with open(filename, 'wt') as write:
		write.write(output)

if __name__ =='__main__':
	import sys
	for arg in sys.argv[1:]:
		fix_links(arg)