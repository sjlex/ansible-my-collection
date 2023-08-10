# ansible-my-collection

> An Ansible Collection of roles.

## Supported Operating Systems

| Platform | Versions                   |
|----------|----------------------------|
| Debian   | Buster, Bullseye, Bookworm |

## Install

- requirements.yml

  ```yml
  collections:
    - name: sjlex.collection
      source: https://github.com/sjlex/ansible-my-collection
      type: git
  ```

## Usage

```yml
roles:
  - role: sjlex.collection.fish
```

or

```yml
tasks:
  - name: "Install packages"
    ansible.builtin.include_role:
      name: "sjlex.collection.fish"
    vars:
      fisher_plugins:
        - sjlex/plain-prompt
        - jethrokuan/z
        - jethrokuan/fzf
```

## Development and testing

### 1. Build docker image and run dev-container:
  
```shell
./bin/task docker:build
./bin/task docker:run
```

### 2. Install dev dependencies

```shell
task dependencies:dev:install
```

### 3. Development

```shell
cd roles/fish
 ```

Run molecule test:

```shell
molecule test
 ```

or

```shell
molecule create &&
molecule converge &&
molecule idempotence &&
molecule verify &&
molecule destroy
 ```

### 4. Testing

```shell
task test:all
 ```

or (specific role):

```shell
task test:role -- fish
 ```

### 5. Linting

```shell
molecule lint
molecule lint:fix
 ```

## License

[MIT](LICENSE)
