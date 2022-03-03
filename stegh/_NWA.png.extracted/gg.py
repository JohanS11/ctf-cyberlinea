import zlib

f = open('29.zlib', 'rb')
decompressed_data = zlib.decompress(f.read())
