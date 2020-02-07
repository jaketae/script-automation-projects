#!/bin/bash

function init(){
    cd
    python create.py $1
    cd /Users/jaketae/documents/github/$1
    git init
    git remote add origin git@github.com:jaketae/$1.git
    touch README.md
    git add .
    git commit -m "initial commit"
    git push -u origin master
    echo "==========Repo intialization complete!=========="
}

init