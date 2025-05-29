#!/usr/bin/python

# Copyright: (c) 2024, Your Name <your@email.com>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt )
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file on remote host with given content and path

version_added: "1.0.0"

description:
  - This module creates a text file on the target machine.
  - It allows specifying both the file path and content.

options:
    path:
        description: Path where the file should be created.
        required: true
        type: str
    content:
        description: Content to write into the file.
        required: true
        type: str

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a test file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/testfile.txt
    content: "This is a test file."
'''

RETURN = r'''
path:
    description: The path of the file that was created.
    type: str
    returned: always
message:
    description: Status message about the result.
    type: str
    returned: always
changed:
    description: Whether the module made any changes.
    type: bool
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule

def write_file(path, content):
    try:
        with open(path, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        raise Exception(f"Could not write file: {e}")

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    try:
        # Write file
        write_file(module.params['path'], module.params['content'])
        result['changed'] = True
        result['path'] = module.params['path']
        result['message'] = "File written successfully"
    except Exception as e:
        module.fail_json(msg=str(e), **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()