##############################################################################
# Clone steinitz.
cd ~/projects
git clone git@github.com:iogf/steinitz.git steinitz-code
##############################################################################
# Push code.
cd /home/tau/projects/steinitz-code
git status

git add *
git commit -a
git push
##############################################################################
# Checkuot changes.
cd /home/tau/projects/steinitz-code
git checkout *
##############################################################################
# Create dev branch.
cd /home/tau/projects/steinitz-code
git branch -a
git checkout -b development
git push --set-upstream origin development
##############################################################################
# Switch to master branch.
cd /home/tau/projects/steinitz-code
git checkout master
##############################################################################
# Switch to development branch.
cd /home/tau/projects/steinitz-code
git checkout development
##############################################################################
# Create branch from existing commit.
cd ~/projects/steinitz-code
git checkout master
git checkout -b old_version e353c2b598c5a78d25690eedadfda28a4fc4e483
git push --set-upstream origin old_version
git checkout old_version
##############################################################################
# Delete old branch.
cd ~/projects/steinitz-code
git checkout master
git branch -d old_version
git push origin :old_version
git fetch -p 
##############################################################################
# Merge development into master.
cd ~/projects/steinitz-code
git checkout master
git merge development
git push
git checkout development
##############################################################################
# It installs steinitz.
cd /home/tau/projects/steinitz-code
sudo bash -i
python2 setup.py install
rm -fr build
exit
cd /home/tau/projects/steinitz-code
##############################################################################
# Share on pypi.
cd ~/projects/steinitz-code
python2 setup.py sdist register upload
rm -fr dist
##############################################################################

