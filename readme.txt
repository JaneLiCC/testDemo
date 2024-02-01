#Hello, it's a test project in GIT

$ cd airtest/
$ git init
# edit file
$ ls
$ git add readme.txt            #need to git add again after modify the existing file, add files to stage
$ git commit -m "add readme"    #commit the stage change to branch
$ git status
$ git diff                      #see not commit modification
$ git log --pretty=oneline      #see commit history
$ git reset --hard HEAD^        #reset to last version, can be HEAD^^, HEAD~100
$ git reset --hard 3500         #reset to assigned version(can be found in git log output)
$ git reset HEAD readme.txt     #reset readme.txt to HEAD version
$ git reflog                    #see all version history 
$ git checkout -- readme.txt    #undo the latest change or readme.txt



