# Morse Code 
Encrypt Morse code and decrypt Morse code using Python.



Option
------
|  key   |   Using      | 
| ------ | ------------ | 
| -t, --text | English Language to Morse code| 
| -m, --morse| Morse code to English Language.|
| -p, --play | Play the sound Morse code.|
| -s, --nostyle| Canceling styles.|

Install
-------
```bash
$ git clone https://github.com/hathemahmed/morse
$ cd morse 
$ python3.6 -m pip install -r requirements.txt
$ chmod +x morse.py
$ ./morse.py --help
```

Using
-----
Encoding:  
```bash
$ ./morse.py -t "Hello World" -p 
```

Decoding:  
```bash
$ ./morse.py -m ".- -.. -- .. -." -p
```





