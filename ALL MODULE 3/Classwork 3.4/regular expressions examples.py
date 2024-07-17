import re
text = "Write a program to build a bridge but beware of the Beyonce's beehive. Behave."
words = re.findall(r"\bb\w*e\b\*e", text)
print(words)