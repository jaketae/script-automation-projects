import sys
import os
from github import Github

access_token = "your_access_token"
path = "/Users/jaketae/documents/github"


def create():
	project_name = str(sys.argv[1])
	os.makedirs(os.path.join(path, project_name))
	user = Github(access_token).get_user()
	user.create_repo(project_name)

if __name__ == '__main__':
	create()
