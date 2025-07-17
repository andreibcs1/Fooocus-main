# Creez fișierul corectat `entry_with_update.py` care apelează `main()` din `launch.py`,
# transmițând argumentele primite din linia de comandă (prompt, preset, etc).
entry_with_update_code = """
import os
import sys

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root)
os.chdir(root)

try:
    import pygit2
    pygit2.option(pygit2.GIT_OPT_SET_OWNER_VALIDATION, 0)

    repo = pygit2.Repository(os.path.abspath(os.path.dirname(__file__)))

    branch_name = repo.head.shorthand
    remote_name = 'origin'
    remote = repo.remotes[remote_name]
    remote.fetch()

    local_branch_ref = f'refs/heads/{branch_name}'
    local_branch = repo.lookup_reference(local_branch_ref)
    remote_reference = f'refs/remotes/{remote_name}/{branch_name}'
    remote_commit = repo.revparse_single(remote_reference)

    merge_result, _ = repo.merge_analysis(remote_commit.id)

    if merge_result & pygit2.GIT_MERGE_ANALYSIS_UP_TO_DATE:
        print("Already up-to-date")
    elif merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:
        local_branch.set_target(remote_commit.id)
        repo.head.set_target(remote_commit.id)
        repo.checkout_tree(repo.get(remote_commit.id))
        repo.reset(local_branch.target, pygit2.GIT_RESET_HARD)
        print("Fast-forward merge")
    elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:
        print("Update failed - Did you modify any file?")
except Exception as e:
    print('Update failed.')
    print(str(e))

print('Update succeeded.')

# ✅ Aici apelăm corect funcția main() din launch.py cu argumentele liniei de comandă
from launch import main
if __name__ == '__main__':
    main(sys.argv[1:])
"""

with open("/mnt/data/entry_with_update.py", "w") as f:
    f.write(entry_with_update_code)

"/mnt/data/entry_with_update.py corect pregătit ✅"
