# Sensei Rescuing API
API that can create ratings and interact with them using user data. It can help create leaderboards in various services

> [!NOTE]
> An example of using the API can be found in [this project](https://github.com/mikhalexandr/PyGame-Sensei-Rescuing)

## 🛠️ Tech Stack
ㅤ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## 🎯 Quick Start
* Clone the project to your computer from Github using the command:
```
git clone https://github.com/mikhalexandr/Flask-Rating-API.git
```

* Install all required dependencies from `requirements.txt`:
```
pip install requirements.txt
```

* Add this environment variables to the configuration:
```
PYTHONUNBUFFERED=1;SECRET_KEY=change_to_your_key
```

* Run `app.py`

## 📝 Documentation
#### 🧩 SQLAlchemy Database Structure
* Users Table
  - name - user's name -> str
  - hashed_password - user's hashed password -> str
  - level_amount - number of levels completed by the user -> int (default=0)
  - time - amount of time spent by the user on completion (in seconds) -> int (default=0)
 
#### 📬 Requests
* **Register Requests**
  - POST "/api/register" (body: name -> str, password -> str)
    + adds a new user (requires name uniqueness check)
* **Login Requests**
  - GET "/api/login" (body: name -> str, password -> str)
    + authorizes the user by checking the username and password
    + returns number of levels completed and time spent completing (body: level_amount -> int, time -> int)
* **Update Resources**
  - PATCH "/api/update/name" (body: name -> str, new_name -> str, password -> str)
    + updates user's name (requires password confirmation and name uniqueness check)
  - PATCH "/api/update/password" (body: name -> str, password -> str, new_password -> str)
    + updates user's password (requires password confirmation and password difference from the old one)
  - PATCH "/api/update/record" (body: name -> str, level_amount -> int, time -> int)
    + updates number of levels completed and time spent completing
* **Delete Requests**
  - DELETE "/api/delete" (body: name -> str, password -> str)
    + deletes user data (requires password confirmation) 
* **Rating Requests**
  - GET "/api/rating" (body: name -> str)
    + gets all users in the sorted list (body of each user in list: name -> str, level_amount -> int, time -> int)
    + gets the user's place in the rating table (body: user_index in list + 1 -> int) 
