import subprocess
import sys

result = subprocess.run(['jupyter', 'notebook', 'list'], stdout=subprocess.PIPE).stdout.decode('utf-8')

lines = result.split('\n')
url_line = lines[1]
url = url_line.split(' ')[0]
token = url.split('=')[1]

print('\t%s/?token=%s\n' % (sys.argv[1], token))
