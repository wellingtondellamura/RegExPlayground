#imports regex lib
import re

# define regex
regex = re.compile(r'[^0-9]')

strCPF = "123.456.789-10"

print("Original: " + strCPF)

# remove all characters that are not numbers
strCPF = regex.sub('', strCPF)

# show result in console
print("Removed: " + strCPF)

