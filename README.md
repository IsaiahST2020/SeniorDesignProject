# SeniorDesignProject
>-SSH Stetup<br/>
>-In .ssh<br/>
>-ssh-keygen -t rsa -b 4096 -C "SeniorDesign Isaiah Linux"<br/>
>-Then copy the generated id_rsa.pub<br/>
>-After adding key to github<br/>
>-Enter command in repo<br/>
>git remote set-url origin git@github.com:IsaiahST2020/SeniorDesignProject.git<br/>

>Steps for setup:<br/>
>source bin/activate<br/>
>cd src<br/>
>python manage.py runserver<br/>
>deactivate <br/>

## Setup with pipenv
To have this environment run as smoothly as possible, you can run the following commands to get a working setup for production or development

### Installing pipenv
to get all the dependencies independant of the system, you will need to install `pipenv`

debian/ubuntu:
```bash
sudo apt install python3-pipenv
```
every other system
```bash
$ pip install pipenv
```
## Installing dependencies with pipenv
Once that is done, navigate to the workspace and run the following commands
```bash
$ pipenv install
```
### Installing dependencies + development libraries
This includes things like `pylint` and `autopep8` to help keep formatting and documentation consistent.
```bash
pipenv install --dev
```
## Running the application
if you want to run the server using the virtual environment provided by pipenv, you can run one of the following
```bash
pipenv run python manage.py runserver
```
or
```bash
pipenv run runserver
```
