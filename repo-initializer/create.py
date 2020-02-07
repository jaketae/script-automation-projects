import sys
import os
from github import Github

username = "jaketae"
password = "" 
path = "/Users/jaketae/documents/github"


def create():
	project_name = str(sys.argv[1])
	os.makedirs(os.path.join(path, project_name))
	user = Github(username, password).get_user()
	user.create_repo(project_name)

if __name__ == '__main__':
	create()
