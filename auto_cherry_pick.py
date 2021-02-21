import gflags
import sys
from getjira import *
from getgerrit import *
FLAGS = gflags.FLAGS
gflags.DEFINE_string("git_repo",
                     None,
                    "Location of the git repo (master branch) "
                    "Example: --git_repo=/home/eandrade/git/main",
                      short_name="gr")
gflags.DEFINE_string("branch_name",
                    None,
                    "Name of the branch in git "
                    "Example: --branch_name=danube-4.0.3-stable",
                    short_name="br")
gflags.DEFINE_string("target_branch",
                    None,
                    "comma separate target branch "
                    "Example: --target_branch=danube-4.0.3-stable",
                    short_name="tr")
gflags.DEFINE_string("change_id",
                    None,
                    "change id of gerrit "
                    "Example:",
                    short_name="ci")
gflags.DEFINE_string("gerrit_id",
                    None,
                    "gerrit id"
                    "Example:",
                    short_name="gid")
gflags.DEFINE_string("revision",
                    None,
                    "commit id of gerrit "
                    "Example:",
                    short_name="pr")
gflags.DEFINE_string("gerrit_username",
                    None,
                    "gerrit http username "
                    "Example:",
                    short_name="gu")
   
gflags.DEFINE_string("gerrit_password",
                    None,
                    "gerrit http password "
                    "Example:",
                    short_name="gp")
def main():
    #print(FLAGS.gerrit_username)
    #print(FLAGS.gerrit_password)
    jira = JIRA(server="https://jira.nutanix.com",basic_auth=("nagasaikiran.karra", "Saikiran123@"))  
    gerrit = GerritClient(base_url="https://gerrit.eng.nutanix.com",username='nagasaikiran.karra',password='/ABNeZHsJzGR7FSHrCnvkhibfPes0XwVy7a8GRODsQ')
    #call functions from here
    print(get_gerrit_id(jira,"ENG-334399")) 
    print(get_commit_msg(gerrit,"493876","4eae18fe7d"))

if __name__ == "__main__":
    try:
        FLAGS(sys.argv)
        main()
    except Exception as EXN:
        print("Unexpected exception occured: %s" % EXN)
        raise