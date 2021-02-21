from gerrit import GerritClient
from gerrit.changes.change import GerritChange
import certifi
import requests
#######Canaveral CA Certificates ####https://confluence.eng.nutanix.com:8443/display/ES/Install+Canaveral+CA+Chain
#response = requests.get('http://canaveral-gatekeeper.canaveral-corp.us-west-2.aws/ca/ca-chain.crt')
#with open(certifi.where(), "ab") as f:
#    f.write(response.content)
##################Getting error without above code###################
def cherry_pick(gerrit,Gerrit_ID,Revision_ID,input_):
    #here input_ is a dictionary with message and destination as keys.
    """
        input_ = {
        "message" : "Implementing Feature X",
        "destination" : "release-branch"
    }
    """
    change = gerrit.changes.get(Gerrit_ID)
    revision = change.get_revision(Revision_ID)
    result = revision.cherry_pick(input_)

def get_change(gerrit,Gerrit_ID):
    #prints few fields of the change
    change = gerrit.changes.get(Gerrit_ID)
    print(change)
    print(change.id)
    print(change.status)
    print(change.subject)
def get_revision(gerrit,Gerrit_ID,Revision_ID):
    change = gerrit.changes.get(Gerrit_ID)
    a=change.get_revision(Revision_ID)
    print(a.project)
    print(a.change)
    print(a.revision)
    print(a.gerrit)
def get_commit_msg(gerrit,Gerrit_ID,Revision_ID):
    #returns the commit msg for that revision
    change = gerrit.changes.get(Gerrit_ID)
    a=change.get_revision(Revision_ID)
    return a.get_commit().message
################################# main code #################################################
#gerrit = GerritClient(base_url="https://gerrit.eng.nutanix.com",username='nagasaikiran.karra',password='/ABNeZHsJzGR7FSHrCnvkhibfPes0XwVy7a8GRODsQ')
#call functions from here 
#print(get_commit_msg(gerrit,"493876","4eae18fe7d"))
################################## END ###################################################
