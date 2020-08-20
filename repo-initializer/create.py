import os
import sys

from github import Github


def create(path):
    project_name = str(sys.argv[1])
    os.makedirs(os.path.join(path, project_name))
    user = Github(os.environ["GITHUB_TOKEN"]).get_user()
    user.create_repo(project_name)


if __name__ == "__main__":
    path = "/Users/jaketae/documents/dev/github"
    create(path)
