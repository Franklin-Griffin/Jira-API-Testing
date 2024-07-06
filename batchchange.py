# This program sets the descriptions of all tasks and subtasks to "This description was modified using Python!"

from jira import JIRA

jira = JIRA(server="https://fgriffin.atlassian.net", basic_auth=("frankiegriffin107@gmail.com", open("token.txt").read()))
key = jira.projects()[0].key # the key of the first project, which is the only project on this account

issues = jira.search_issues(f'project={key}') # this returns the IDs all tasks including subtasks

for issue_key in issues:
    issue = jira.issue(issue_key)
    issue.update(description="This description was modified using Python!")

print("Issue descriptions have been updated successfully.")