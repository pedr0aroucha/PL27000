# readme

### 🛠 TECHNOLOGIES USED
<ul>
  <li>Python - Django </li>
  <li>HTML/CSS</li>
</ul>

### 🧰 DEPENDENCIES
<ul>
  <li> <a href="https://www.python.org/downloads/"> Python </a> </li>
</ul>

### 🚀 GET STARTING

1. Make a clone :

```sh
  $ git clone https://github.com/pedr0aroucha/organization_system.git
```

2. Execute the aplication:

```sh
  # enter the folder
  $ cd organization_system

  # starting the virtual development environment
  $ python3 -m venv .env
  $ source .env/bin/activate

  # Install the dependencies
  $ pip install -r requirements.txt

  # enter the folder
  $ cd PL27000
  
  # creating and synchronizing the database
  $ python manage.py migrate
  $ python manage.py makemigrations && python manage.py migrate

  # Start the aplication
  $ python manage.py runserver

```
