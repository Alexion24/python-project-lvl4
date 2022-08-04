### Hexlet tests and linter status:
[![Actions Status](https://github.com/Alexion24/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/Alexion24/python-project-lvl4/actions)
[![CI](https://github.com/Alexion24/python-project-lvl4/actions/workflows/CI.yml/badge.svg)](https://github.com/Alexion24/python-project-lvl4/actions/workflows/CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/5d55f3f3731e14615681/maintainability)](https://codeclimate.com/github/Alexion24/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5d55f3f3731e14615681/test_coverage)](https://codeclimate.com/github/Alexion24/python-project-lvl4/test_coverage)

### Description:
Task manager is a web application for managing tasks between people.

### Application link:
https://alexion-task-manager.herokuapp.com

### Local installation via poetry:
Clone repo:

```
git clone https://github.com/Alexion24/python-project-lvl4.git
cd python-project-lvl4
```
Usage:

The file ".env" should be created in root directory. You should list there local variables:
```
SECRET_KEY='your django secret here'
ACCESS_TOKEN='your token from Rollbar error tracker here'
```
Install dependencies:
```
make install
```
Initialize migrations:
```
make migrate
```
Run app at http://127.0.0.1:8000/:
```
make runserver
```