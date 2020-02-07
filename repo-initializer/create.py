import sys
import os
from github import Github

username = "jaketae"
password = "Jakelake100493" # Make sure to erase this
path = "/Users/jaketae/documents/github"


def create():
	project_name = str(sys.argv[1])
	os.makedirs(os.path.join(path, project_name))
	user = Github(username, password).get_user()
	try:
		user.create_repo(project_name)
		print("Successfully created repo {}".format(project_name))
	except:
		print("Something's gone astray. Try again.")

if __name__ == '__main__':
	create()
