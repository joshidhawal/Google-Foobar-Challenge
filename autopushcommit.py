import os

commitMessage = input('Enter the Commit Message without quotes:\n')

command = 'git commit -m "'+str(commitMessage)+'"'
print (command)
os.system('git add .')
os.system(command)
os.system('git push origin')