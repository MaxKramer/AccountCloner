import urllib2
import json
from git import Repo
import os

def get_valid_input(message):
	inp = raw_input(message)
	while True:
		if isinstance(inp, str) and len(inp) > 0:
			break
		else:
			inp = raw_input(message)
	return inp

username = get_valid_input("Your Github Username: ")
repoJson = urllib2.urlopen("https://api.github.com/users/" + str(username) + "/repos").read()
repositories = json.loads(repoJson)

git_export_path = get_valid_input("Please enter the full directory path to store the repos (/Users/Max/github/):")

for r in repositories:
	print "Cloning " + r["name"] + " from " + r["git_url"]
	Repo.clone_from(r["git_url"], str(git_export_path) + r["name"])