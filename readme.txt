#Hello, it's a test project in GIT


#local file  +git add-----> stage  +git commit----->local branch  + git push----->remote branch

$ cd airtest/
$ git init
# edit file
$ ls
$ git add readme.txt            #need to git add again after modify the existing file, add files to stage
$ git commit -m "add readme"    #commit the stage change to branch
$ git status
$ git diff                      #see modification between local and branch
$ git log --pretty=oneline      #see commit history
$ git reset --hard HEAD^        #reset to last version, can be HEAD^^, HEAD~100
$ git reset --hard 3500         #reset to assigned version(can be found in git log output)
$ git reset HEAD readme.txt     #reset readme.txt in stage to HEAD version
$ git reflog                    #see all version history 
$ git checkout -- readme.txt    #undo the latest change or readme.txt
$ git rm help.txt -f            #delete file on local and on stage
$ git commit -m "d"             #commit rm on branch, still on the local, not the remote repository
$ git branch -M main
$ git remote add origin https://github.com/JaneLiCC/testDemo.git
$ git push -u origin main

#key
$ ssh-keygen -t rsa -C "xxx@xxx.com"  #gen key in current dir
login github->head photo->settings->SSH and GPG keys->New SSH key->paste pub key




