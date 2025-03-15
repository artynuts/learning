# GIT

### Clone a git repository

```
git clone https://github.com/artynuts/learning.git
```

#### Setup Initial Config

```
git config --global user.name "<name>"
git config --global user.email "<email>"
```

### List config

```
git config --list
```


### Get the log of changes in git repository

```
git log
```

### Remove a commit entirely

1. Start a rebase `git rebase -i <COMMIT_ID>^`
2. Editor open with the list of commits. Delete the commit you want to remove. Save. If vim `:wq`
3. Force push the change `git push origin main --force`

### Abort a rebase

```
git rebase --abort
```

### Create new branch

```
git checkout -b <branch-path/branch-name> # feature/server-persistence
```
### Publish the branch 

```
git push -u origin <branch-path/branch-name> #feature/server-persistenc
```

### Restore

Restore specified files to their state in the last commit.

```
git restore . # Restore all files in current directory and subdirectories
git restore file.txt # Restore specific file
git restore --staged . # Unstage all changes (but keep modifications)
git restore --source=main file.txt # Restore file from specific branch/commit
```

### Clean

Remove untracked files and directories from current working directory

```
git clean -fd
```

### Status

Shows the current status of your working directory and staging area. 
1. Which branch you are on
2. Changes staged for commit
3. Changes not staged for commit

```
git status
```


