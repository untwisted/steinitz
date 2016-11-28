##############################################################################
# clone steinitz.
cd ~/projects
git clone git@github.com:iogf/steinitz.git steinitz-code
##############################################################################

# push, steinitz, github.
cd /home/tau/projects/steinitz-code
git status

git add *
git commit -a
git push
##############################################################################
# checkout, steinitz.
cd /home/tau/projects/steinitz-code
git checkout *
##############################################################################
# create, development, branch, steinitz.
cd /home/tau/projects/steinitz-code
git branch -a
git checkout -b development
git push --set-upstream origin development
##############################################################################
# switch, master, branch, steinitz.
cd /home/tau/projects/steinitz-code
git checkout master
##############################################################################
# switch, development, branch, steinitz.
cd /home/tau/projects/steinitz-code
git checkout development
##############################################################################
# create, new branch, from, existing commit, master, steinitz.
cd ~/projects/steinitz-code
git checkout master
git checkout -b old_version e353c2b598c5a78d25690eedadfda28a4fc4e483
git push --set-upstream origin old_version
git checkout old_version
##############################################################################
# delete, old version, steinitz.
cd ~/projects/steinitz-code
git checkout master
git branch -d old_version
git push origin :old_version
git fetch -p 
##############################################################################
# merge, development, into, master, steinitz, snz.
cd ~/projects/steinitz-code
git checkout master
git merge development
git push
git checkout development
##############################################################################
# it installs steinitz.
cd /home/tau/projects/steinitz-code
sudo bash -i
python2 setup.py install
rm -fr build
exit
cd /home/tau/projects/steinitz-code
##############################################################################
# remove, steinitz, files.
sudo bash -i
rm -fr /usr/local~/projects/python2.7/dist-packages/steinitz
exit
##############################################################################
# share, put, place, host, package, python, pip, application, steinitz.

cd ~/projects/steinitz-code
python2 setup.py sdist register upload
rm -fr dist
##############################################################################

