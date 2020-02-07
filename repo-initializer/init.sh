#!/bin/bash

project=$1


function init(){
    python create.py $project
    cd /Users/jaketae/documents/github/$project
    git init
    git remote add origin git@github.com:jaketae/$project.git
    touch README.md
    git add .
    git commit -m "initial commit"
    git push -u origin master
    echo "==========Repo intialization complete!=========="
}

init