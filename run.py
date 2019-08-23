import subprocess
import os

push = "git push"
pull = "git pull"

add = "git add ."
commit = 'git commit -m "Just another commit"'

commit_count = 0

result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
>>> result.stdout

