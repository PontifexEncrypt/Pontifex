#!/bin/sh

rg --multiline '(?s)# golf start\n(.*)\n# golf end' -or '$1' solitaire-golf-fprasx.py | wc -c

