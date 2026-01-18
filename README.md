# sql-evaluator
Tool to evaluate data differences of sql queries 


1. Install and config pyenv and pyenv-virtualenv
see file X for the correct env

2. Install robot framework
pip install robotframework

Verify with: robot --version

3. Install VSCode extension for RobotFramework

https://docs.robotframework.org/docs/getting_started/ide

---

Run tests:
robot .

Run with a listener:
robot --listener simple_listner.py tests.robot


source .env