# Sensei Rescuing API
API that can create ratings and interact with them using user data. It can help create leaderboards in various services

> [!NOTE]
> An example of using the API can be found in [this project](https://github.com/mikhalexandr/PyGame-Sensei-Rescuing)

## 🛠️ Tech Stack
ㅤ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

## 🎯 Quick Start
* Clone the project to your computer from Github using the command:
```
git clone https://github.com/mikhalexandr/Flask-Rating-API.git
```

* Install all required dependencies from `requirements.txt`:
```
pip install requirements.txt
```

* Run `app.py`

## 📝 API Documentation
#### User Requests
* POST "/api/user/add" (body: name -> str, password -> str, level_amount -> int, time -> int)  
  - adds a new user to the leaderboard
* PUT "/api/user/upload/<user_name>" (body: level_amount -> int, time -> int)  
  - uploads user information about level_amount and time
#### Leaderboard Requests
* GET "/api/leaderboard/<user_name>"  
  - gets all users in the sorted list (name -> str, level_amount -> int, time -> int)
  - gets the user's place in the leaderboard 
