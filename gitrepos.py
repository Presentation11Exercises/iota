import urllib2
import BeautifulSoup
import sys
if len(sys.argv) > 1:
  site = str(sys.argv[1])
else:
  print "No arguments found. Must specify github user url."
  quit()
pagedata = urllib2.urlopen(site).read()
repo_names = []
for repotag in BeautifulSoup.BeautifulSoup(pagedata).findAll("span", { "class" : "repo" }):
  repo_names.append(repotag.getText())

def printarray(arr):
  for entry in arr:
    print entry

if len(repo_names) > 0:
  printarray(repo_names)
else:
  print "No repos found on page: " + site
