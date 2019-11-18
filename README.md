# Morse Code 


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
$ cd morse & chmod +x morse.py
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





