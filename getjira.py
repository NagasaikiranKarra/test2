from jira import JIRA
from collections import Counter
def get_cherrypick_issues(jira):
    all_cherrypick_tickets = jira.search_issues('status=autocherrypick order by ASC',fields = ['comment','key','id','summary'])
    return all_cherrypick_tickets
def get_gerrit_id(jira,issue_num):
    issue = jira.issue(issue_num)
    comments = issue.fields.comment.comments
    git_check="===git tracker==="
    gerrit_id=[]
    print("Gerrit ID's are below:")
    for i in range(len(comments)):
        para=comments[i].body
        para=para.splitlines()
        com_tick=dict()
        if(git_check in para[0]):
            for line in para:
                a=line.split(": ")
                if(len(a)==2):
                    key=a[0]
                    value=a[1]
                    com_tick[key]=value
            if('Code Review URL' in com_tick.keys()):
                id=int(com_tick['Code Review URL'].split("/")[-1])
                gerrit_id.append(id)
    return gerrit_id
def get_issue(jira,issue_num):
    issue=jira.issue(issue_num,fields = ['comment','key','id','summary'])
    print(issue.fields.issuetype)
    print(issue.fields.fixVersions)
    print(issue.fields.versions)
    print(issue.fields.priority)
    print(issue.fields.summary)
    print(issue.fields.status)
    print(issue.fields.assignee)
    print(issue.fields.worklog)
def get_comments(jira,issue_num,comment_id):
    #issue_num = "ENG-334399" comment_id='2844011'
    return jira.comment(issue_num,comment_id).body
def get_comments_all(jira,issue_num):
    issue = jira.issue(issue_num)
    comments = issue.fields.comment.comments
    for comment in comments:
        print("Comment text : ",comment.body)
def update_issue(issue_num,fields_dict):
    issue = jira.issue(issue_num)
    #issue.update(fields={'summary': 'new summary', 'description': 'A new summary was added'})
    issue.update(fields=fields_dict)
def add_comment(jira,issue_num,comment_msg):
    issue = jira.issue(issue_num)
    jira.add_comment(issue, "Comment text")
######################################## Main Code ##################################################
#jira = JIRA(server="https://jira.nutanix.com",basic_auth=("nagasaikiran.karra", "Saikiran123@"))  
#print(get_gerrit_id(jira,"ENG-334399"))
######################################### End ##########################################################