final = '"';
file = open('Test.txt', 'r');
lines = file.readlines();
lines = [line.replace('\t', ' ') for line in lines];
lines = [line.replace('\n', '", "') for line in lines];
for line in lines:
    final+=line;
final += '"'
file.close();
file = open('Test.txt', 'w')
print(final);
file.write(final);
file.close();
