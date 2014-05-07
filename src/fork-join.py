__author__ = 'Artem'
import sys
import pickle
import os.path
from subprocess import call
import subprocess

version = 0.1
description = """fork/join/drop is a simplified git workflow model
fork <br name>
join
drop
"""

stack = []
script_filename = "fork-join.py"
working_dir = None
git_repo_dir = None
stack_file_path = None
mainline_branch = "master"  # if stack is empty - return master branch

# pops branch name from stack
def pop():
    if stack:
        item = stack.pop()
        save_stack()
        return item
    else:
        return mainline_branch

def get_first():
    if stack:
        for item in stack:
            return item
    return mainline_branch

# pushes branch name to stack
def push(name):
    stack.append(str(name))
    save_stack()

def save_stack():
    with open(get_stack_file(), 'wb+') as f:
        pickle.dump(stack, f)

def get_git_repo_dir():
    p = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if err:
        print err
        sys.exit(1)
    return out.replace("\n", "")

def get_stack_file():
    global stack_file_path
    if not stack_file_path:
        stack_file_path = os.path.join(git_repo_dir, ".stack")
    return stack_file_path

def init():
    if os.path.isfile(get_stack_file()):
    #open(stack_file_path, 'a').close() #Creates empty file if it's not exists
        with open(get_stack_file(), 'rb') as f:
            stack2 = pickle.load(f)
        for x in stack2:
            stack.append(x)

def fork(name):
    print "[fork] " + str(name)
    push(name)
    print "stack:"
    print stack
    call(["git", "branch", name])
    call(["git", "checkout", name])


def join():
    print "[join] "
    print stack
    current_branch = pop()
    previous_branch = get_first()
    print "current_branch: " + current_branch
    print "previous_branch: " + previous_branch
    print "Current branch must be on top of stack!!!"
    call(["git", "checkout", previous_branch])
    call(["git", "merge", "--no-ff", current_branch])

def drop(commandline):
    print "[drop] " + str(commandline)
#.replace(script_filename, "")

if __name__ == "__main__" and len(sys.argv) >= 2:
    sys.argv.pop(0)  # removes script filename (with absolute path) from commandline
    method = sys.argv.pop(0)
    working_dir = sys.argv.pop(0)
    git_repo_dir = get_git_repo_dir()

    if method == "fork":
        init()
        fork(sys.argv[0])
    elif method == "join":
        init()
        join()
    elif method == "drop":
        init()
        drop(sys.argv)
