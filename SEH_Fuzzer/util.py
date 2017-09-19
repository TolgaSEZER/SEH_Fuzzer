import struct
import string

def p32(data):
	return struct.pack("<I", data)
	
def pStr(word, size=4):
    if len(word)>size:
        return None
    value = 0
    for c in word[::-1]:
        value = value*16*16 + ord(c)
    return value

def pattern_create(max_length=5000):
	charset1 = string.ascii_uppercase
	charset2 = string.ascii_lowercase
	charset3 = string.digits
	charset3 += ",.;+=-_!&()#@({})[]%"
	pattern = []
	
	while len(pattern)<max_length:
		for char_1 in charset1:
			for char_2 in charset2:
				for char_3 in charset3:
					if len(pattern) < max_length:
						pattern.append(char_1)
					if len(pattern) < max_length:
						pattern.append(char_2)
					if len(pattern) < max_length:
						pattern.append(char_3)
						
	return "".join(pattern)

def pattern_find(pattern, max_length=5000):
	pattern = p32(pattern)
	origin_pattern = pattern_create(max_length)
	offset = origin_pattern.find(pattern)
	return offset