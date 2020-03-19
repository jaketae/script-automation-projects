#!/bin/bash

project=$1


function init(){
    python create.py $project
    cd /Users/jaketae/documents/github/$project
    git init
    git remote add origin git@github.com:jaketae/$project.git
    touch LICENSE
    touch README.md
    touch .gitignore
    echo .DS_Store >> .gitignore
    touch .editorconfig
    cat << EOF > .editorconfig
# https://editorconfig.org/

root = true

[*]
indent_style = space
indent_size = 4
insert_final_newline = true
trim_trailing_whitespace = true
end_of_line = lf
charset = utf-8

# Docstrings and comments use max_line_length = 79
[*.py]
max_line_length = 119

# Use 2 spaces for the HTML files
[*.html]
indent_size = 2

# The JSON files contain newlines inconsistently
[*.json]
indent_size = 2
insert_final_newline = ignore

[**/admin/js/vendor/**]
indent_style = ignore
indent_size = ignore

# Minified JavaScript files shouldn't be changed
[**.min.js]
indent_style = ignore
insert_final_newline = ignore

# Makefiles always use tabs for indentation
[Makefile]
indent_style = tab

# Batch files use tabs for indentation
[*.bat]
indent_style = tab

[docs/**.txt]
max_line_length = 79
EOF
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    echo "==========Repo intialization complete!=========="
}

init