"""
Learn about bytes.
Bytes are similar to str type, but they are a sequenc3e of
bytes instead of Unicode code points.

Use for raw binary data, fixed-width, single-byte encoding: ASCII

Use the byte() constructor
"""
d = b'data'
print(d, type(d))

info = b'some bytes here'
# Split the bytes using split() method for bytes
print(info.split())

# Encoding: alt + 162 = ó
message = "Vamos al zoológico"
print(message)
data = message.encode("utf-8")
print(data)
data_decoded = data.decode("utf-8")
print(data_decoded)