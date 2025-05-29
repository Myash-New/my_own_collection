# My Own Collection

This collection contains custom Ansible modules and roles.

## Modules

### `my_own_module`

Creates a text file with specified content on a remote host.

#### Parameters

- `path`: Path to create the file.
- `content`: Content to write into the file.

## Roles

### `create_file`

Uses `my_own_module` to create a file with default parameters.