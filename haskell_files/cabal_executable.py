import sys

with open(sys.argv[1], 'r') as cabalfile:
    cabal_lines = cabalfile.readlines()

lookfor = sys.argv[2].strip()

for line in cabal_lines:
    if 'executable' in line or 'test-suite' in line:
        nospaces = line.strip().replace(' ','')
        nows = nospaces.replace('\t','')
        exename = nows[len('executable'):]
        if exename[-len(lookfor):] == lookfor:
            print(exename)
            sys.exit()


print('echo "%s not found in Cabal file"' % (lookfor,))

