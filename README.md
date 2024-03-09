## Terminal
- `dir` -> zeigt die Ordnerihnhalte
- `cd` -> change directory
- `cd ..` -> wechsele Directory ein Ordner hoch
- `cd ..\..` ->  wechsele Directory ZWEI Ordnern hoch (grant-parent directory)
- `cd \` -> wechsele to the ROOT directory
- `cd FOLDER_NAME` -> enters the folder
- `cd F` and press TAB => autocompletes to `cd FOLDER_NAME` if 
- `cd ..\FOLDER_NAME\` -> go 1 Folder up and one folder down  
- `copy SOURCENAME TARGETNAME` => copies from existing file into new filename
- `dir /a` => shows all files and hidden files (.history, .git, .whatever)


## Git
- `git init` -> creates new local git repository (contains a .git folder)
- `git log` => shows commited history with commit messages and date, author stuff

#### Git commit flow
- `git status` -> shows status of current local git repository
- `git diff` => shows current changes in all files in working directory (subset of changes and not whole project-directory)
- `git add README.md` -> adds ONE file to next commit stage (put the changes on the busstop)
- `git add .` -> adds ALL the changes/files to next commit stage (put the changes on the busstop)
- `git commit -m "your changelogs details"` => makes a commit with a commit message. All staged files will be included. Also partial commits are possible.
- `git push` => syncs with github


## run python programm
- `nodemon index.py` => restarts program after file change detection

## install external python library with pip

`python -m ensurepip`  => one time command, verify that pip is in the windows path correctly set  
`$ python -m ensurepip` => run command in terminal because it starts with `$`

