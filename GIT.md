# GIT

#### Clone a git repository
`` git clone https://github.com/artynuts/learning.git ``

#### Get the log of changes in git repository
`` git log ``

#### Remove a commit entirely
1. Start a rebase `` git rebase -i <COMMIT_ID>^ ``  
2. Editor open with the list of commits. Delete the commit you want to remove. Save. If vim :wq  
3. Force push the change `` git push origin main --force ``

#### Abort a rebase
`` git rebase --abort ``

#### List config
`` git config --list ``
