import os
import sys

file_template = """---
- name: Run Arch Tasks
  ansible.builtin.import_tasks: arch.yml
  when: ansible_os_family == 'Archlinux'
"""

names = sys.stdin.read().splitlines()

for name in names:
    # print(f'{name}')
    # path_handlers = os.path.join("ansible", "roles", name, "handlers")
    path_tasks = os.path.join("ansible", "roles", name, "tasks")
    # os.makedirs(path_handlers, exist_ok=True)
    os.makedirs(path_tasks, exist_ok=True)

    with open(os.path.join(path_tasks, 'main.yml'), 'w') as f:
        f.write(file_template)
    with open(os.path.join(path_tasks, 'arch.yml'), 'w') as f:
        f.write("---")