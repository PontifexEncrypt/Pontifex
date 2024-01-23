#!/bin/sh

rg --multiline '(?s)# golf start\n(.*)\n# golf end' -or '$1' solitaire-fprasx.py | wc -c

