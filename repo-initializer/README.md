# Repo Initializer

This script can be used to initialize an empty GitHub repository. It is as simple as running 

```bash
init my-repo
```

## Alias

It is highly recommended that you set up an alias. This is the alias settings I have on my personal workstation. Feel free to edit according to the structure of your directory.

```bash
alias init='cd /Users/jaketae/documents/github/script-automation-projects/repo-initializer; ./init.sh $1'
```

## Token

`PyGithub` requires user information to log into your account and create a new repository. To do this, you need to create an access token. Please follow the instructions on the [GitHub website](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line).

After you have generated an access token, edit the `access_token` variable in `create.py`. 

## Bug Reports

Feel free to contact me with bug reports through email, or even better, open a pull request!