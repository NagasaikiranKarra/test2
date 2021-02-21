from gerrit import GerritClient
from gerrit.changes.change import GerritChange
import certifi
import requests
#######Canaveral CA Certificates ####https://confluence.eng.nutanix.com:8443/display/ES/Install+Canaveral+CA+Chain
#response = requests.get('http://canaveral-gatekeeper.canaveral-corp.us-west-2.aws/ca/ca-chain.crt')
#with open(certifi.where(), "ab") as f:
#    f.write(response.content)
##################Getting error without above code###################
#main code start
gerrit = GerritClient(base_url="https://gerrit.eng.nutanix.com",username='nagasaikiran.karra',password='/ABNeZHsJzGR7FSHrCnvkhibfPes0XwVy7a8GRODsQ')
change = gerrit.changes.get("493876")
#print(change.id)
#print(change.status)
#print(change.list_comments())
ab=change.get_revision("4eae18fe7d")
#print(ab.get_commit().list_change_files())
cd=ab.get_commit()
print(cd.message)

"""
Things Done
1.Fetch the change and print project,change ID, status,subject etc..
2.Fetch commit messages from the change and its revisions.
3.Cherry pick a change or any of its revisions to a branch(Code is ready but yet to be tested)
###############################################################
change = gerrit.changes.get("493876")
print(change)
print(type(change))
print(change.id)
print(change.status)
print(change.subject)
######Revision##################################################
print(change.get_revision("808b4792f4"))
a=change.get_revision("e6a02af071")
print(a.project)
print(a.change)
print(a.revision)
print(a.gerrit)

#########Cherry pick############################################
input_ = {
    "message" : "Implementing Feature X",
    "destination" : "release-branch"
}

change = gerrit.changes.get('myProject~stable~I10394472cbd17dd12454f229e4f6de00b143a444')
revision = change.get_revision('3848807f587dbd3a7e61723bbfbf1ad13ad5a00a')
result = revision.cherry_pick(input_)

##################################################################
#print("included in")
change1 = gerrit.changes.get("493876")
#a=change1.get_include_in()
#print(a)
#a=change1.list_comments()
#print("comments")
#print(a)
#print("robot comments")
#a=change1.list_robot_comments()
#print(a)
#a=change1.messages
##################################################
#Revision
change = gerrit.changes.get("493876")
ab=change.get_revision("4eae18fe7d")
print(ab.get_revision_actions())
print(ab.get_commit())
print(ab.list_reviewers())
print(ab.get_description())
####################################################
#Cherry-pick Revision
input_ = {
                "message" : "Implementing Feature X",
                "destination" : "release-branch"
            }
change = gerrit.changes.get('493876')
revision = change.get_revision('3848807f587dbd3a7e61723bbfbf1ad13ad5a00a')
result = revision.cherry_pick(input_)
"""