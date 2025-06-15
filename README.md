## Git Exercise understanding the concept of Branching and Merging

## Team Members:
```bash
1. Saima Nasreen
2. Chandrakant Majumdar
   ```
## WorkFlow:
```bash
1. Created a folder Project-1 on local machine and linked with Git repository Git_Exercise_Branching_Merging.
2. Created a folder named as saima-chandrakant_Git_Exercise in the main branch in the local machine.
3. Created a new branch dev/saima and created a subfolder named as Frontend_ inside it.
4. Created another branch dev/chandra and created another subfolder named as Backend_ inside it.
5. After verifying both subfolders codes, both branches are merged to the main branch.
```
### Project Structure:
saima-chandrakant_Git_Exercise/<br>
├── Frontend_/<br>
│ └── index.html<br>
└── Backend_/<br>
 └── main.py<br>

## Steps followed:
### 1. Clone the repository
```bash
git clone https://github.com/saimanasreen001/Git_Exercise_Branching_Merging.git
```

### 2. Switch to the branches:
```bash
git switch dev/saima
git switch dev/chandra
```
### Command to create a new branch
```bash
git switch -C new-branch-name
```
### Command to merge any branch to the main branch
```bash
1. Check the current branch : git branch
2. If not main, switch to main : git switch main
3. Now merge to main : git merge merger-branch-name
```

### Conclusion:
```bash
Here we learnt about how branching technique allows multiple developers to work on different features of
the project and how merging helps to merge different branches code to the main branch/ any other branch.
```





