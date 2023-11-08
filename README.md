# TextBlob experimentation


## Purpose

With upcoming Hall-Hoag work, wanted to explore keyword-extraction using TextBlob for possible inclusion into processing-pipeline.


## Usage
- assumes a virtual-environment is set up (at sibling level to code) and populated from `requirements.txt`
- $ cd /path/to/textblob_experimentation_code/
- $ source ../env/bin/activate
- $ python ./keywords.py


## Output

```
HHoag OCRed text ------------------------------------
2023-11-08 14:12:19,714 : INFO : metro: 36
2023-11-08 14:12:19,714 : INFO : government: 15
2023-11-08 14:12:19,714 : INFO : county: 14
2023-11-08 14:12:19,714 : INFO : state: 11
2023-11-08 14:12:19,714 : INFO : city: 10
2023-11-08 14:12:19,714 : INFO : charter: 9
2023-11-08 14:12:19,714 : INFO : power: 9

Obama speech ----------------------------------------
2023-11-08 14:12:19,784 : INFO : america: 18
2023-11-08 14:12:19,784 : INFO : country: 13
2023-11-08 14:12:19,784 : INFO : tonight: 7
2023-11-08 14:12:19,784 : INFO : nation: 7
2023-11-08 14:12:19,784 : INFO : future: 7
2023-11-08 14:12:19,784 : INFO : work: 7
2023-11-08 14:12:19,784 : INFO : family: 5
```

## links

- github: <https://github.com/sloria/TextBlob>
- PyPi: <https://pypi.org/project/textblob/>
- readthedocs: <https://textblob.readthedocs.io/en/dev/>

---