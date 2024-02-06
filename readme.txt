#Hello, it's a test project in GIT


#local file  +git add-----> stage  +git commit----->local branch  + git push----->remote branch

$ cd airtest/
$ git init
# edit file
$ ls
$ git add readme.txt            #need to git add again after modify the existing file, add files to stage, can be a dir
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
$ git push -u origin main       #first push
$ git push                      #normal push
$ git config --global --list    #display config of globle, token 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
$ git clone -b spcx_demo --single-branch url # clone branch

$ git config --global credential.helper cache
$ git config --global credential.helper store   #save name and token
$ git pull                                      #update code from remote, need not to input name everytime

#key
$ ssh-keygen -t rsa -C "xxx@xxx.com"  #gen key in current dir
login github->head photo->settings->SSH and GPG keys->New SSH key->paste pub key

Air Deploy:
1. Ansible and git are installed on oob-mgmt-server when the simulation is started, 
   switches and hosts are connected with oob using oob-switch, ping is ok between them, ssh hostname is ok
   sudo apt install python3-netaddr  #install netaddr on oob-server
2. git clone: need to generate token first on website and use it as password, 
   see https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
3. add hosts (ansible-inventory -i hostsfile --list)
4. add ansible.cfg, otherwise will using key auth
5. ansible pod1 -i inventory/hosts -m ping, to test connection (ansible pod1 -i inventory/hosts -m command -a "pwd")
6. switch ping error: Failed to create temporary directory. In some cases, you may have been able to authenticate and did not have permissions on the target directory.
   We need to config ZTP on oob-mgmt-server to change pass when first login switch and 
    config ZTP:
        DHCP server: 
            sudo cat /etc/dhcp/dhcpd.conf (add: option cumulus-provision-url "http://192.168.200.1/cumulus-ztp";)
            copy ztp to /var/www/html/cumulus-ztp
            sudo service isc-dhcp-server restart
        Switches:
            rebuild to trigger DHCP
7. edit roles 
    roles:
        cd 
        ansible-galaxy role init server     #will automatic generate dirs and files of role(server)
8. run playbooks
    ansible-playbook spec.yml -i inventory/hosts --check
    parameters: ansible-playbook -i inventory/hosts spec.yml -e pname=pvalue
        clear=1         will clear switch settings
        evpnEnable=1    will enable evpn on switch
9. ping test, login in server01 and run ./home/ubuntu/ping.sh




