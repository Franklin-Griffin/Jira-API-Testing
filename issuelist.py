# This program prints the names of all tasks and subtasks alongisde their keys

from jira import JIRA

jira = JIRA(server="https://fgriffin.atlassian.net", basic_auth=("frankiegriffin107@gmail.com", open("token.txt").read()))
key = jira.projects()[0].key # the key of the first project, which is the only project on this account

issues = jira.search_issues(f'project={key}') # this returns the IDs all tasks including subtasks
issues = issues[::-1] # search_issues sorts by date created/ID descending, while date created/ID ascending is likely preferred for this task

for issue_key in issues:
    issue = jira.issue(issue_key, fields="summary") # only request the summary to save time
    print(f"{issue_key}: {issue.fields.summary}")