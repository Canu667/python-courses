>>> import reader
>>> r = reader.Reader('reader/__init__.py')
>>> r.read()

>>> import reader
>>> r = reader.Reader('test.bz2')
>>> r.read()
'data compressed with bz2'
>>> r.close()

WS-0485:reader_example mcanova$ python3 . test.gz (thanks to __main__.py)