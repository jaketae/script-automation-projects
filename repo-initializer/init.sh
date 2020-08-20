#!/bin/bash

project=$1


function init(){
    python create.py $project
    cd /Users/jaketae/documents/dev/github/$project
    git init
    git remote add origin git@github.com:jaketae/$project.git
    touch LICENSE
    touch README.md
    touch .gitignore
    cat << EOF > .gitignore
.DS_Store

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask:
instance/
.webassets-cache

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
Pipfile
Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Intellij project settings
.idea/
.iml

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# static files generated from Django application using `collectstatic`
media
staticfiles
/tags
EOF
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