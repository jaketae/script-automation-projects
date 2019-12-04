#!/bin/sh

nb=$1

function convert(){
	python convert.py $nb
	mv $nb.xlsx ${nb%.pdf}.xlsx
	echo "==========Conversion complete!=========="
}

convert