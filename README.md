# by-n-they-come

A simple tool to sort files into groups. Normally I use this for sorting bracketed photographs into folders so that other scripts can automatically merge them.

Example:
```
$ ls
1.tif  2.tif  3.tif  4.tif  5.tif  6.tif  7.tif  8.tif  9.tif
$ by-n-they-come 3 *.tif
$ tree
├── 00
│   ├── 1.tif
│   ├── 2.tif
│   └── 3.tif
├── 01
│   ├── 4.tif
│   ├── 5.tif
│   └── 6.tif
└── 02
    ├── 7.tif
    ├── 8.tif
    └── 9.tif
```

## Install

This is a basic Python3 package that uses setuptools. To install into a virtual environment:
```
git clone git@github.com:seilis/by-n-they-come.git

python3 -m venv my-env
. ./my-env/bin/activate
pip3 install --upgrade ./by-n-they-come
```

## Usage

Full usage options are sparse but can be seen with `by-n-they-come -h`:

```
by-n-they-come -h
usage: by-n-they-come [-h] N FILES [FILES ...]

positional arguments:
  N           How many in each bin
  FILES       The files to group

optional arguments:
  -h, --help  show this help message and exit
```
