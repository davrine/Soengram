# Soengram

> A photo sharing social networking website

## About this Project

Social media platforms provide instant gratification and analytical data among users - businesses, celebrities, influencers and everyday individuals - as they are able to gauge engagement and impact through their posts and comments received by other users. Follower count is a measure by which users can gauge their popularity among other users on the platform. Soengram provides users all these tools by allowing users to easily interact with others through posting photos on their account timeline and spark conversation through commenting on posts. Users are also able to stay up to date and informed by following friends, family and favorite celebrities and influencers.

### Objective

Develop a photo sharing social networking website where businesses, celebrities, influencers and regular everyday individuals can post photos, comment on posts and follow other users.

### Features

- Post pictures with description
- Follow other users on the platform
- Comment on other users posts

### Built With

- [Python 3](https://www.python.org/)
- [PostgreSQL 13.0 or later](https://www.postgresql.org/)
- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinga 2.11.2](https://jinja.palletsprojects.com/en/2.11.x/)
- [Font Awesome 6](https://fontawesome.com)
- [BootStrap 5](https://getbootstrap.com)

## Getting Started

### Prerequisites

Before you continue, ensure you have installed the following requirements:
- [Python 3](https://www.python.org/)
- [PostgreSQL 13.0 or later](https://www.postgresql.org/)

### Setup

1. Clone the repository 
    ```sh
    $ git clone https://github.com/LujainKhalaf/Soengram.git
    ```
2. Create a virtualenv and activate it
    ```sh
    $ cd Soengram

    # Windows
    $ py -3 -m venv venv
    $ venv\Scripts\activate
    ```
3. Install all packages
    ```sh
    $ pip install -r requirements.txt
    ```
4. Setup a local PostgreSQL database
5. Copy `.env.sample`, rename to `.env` and edit the following lines
    ```
    DB_TYPE="postgresql"
    DB_HOST="localhost"
    DB_PORT="5432"
    DB_USERNAME="your_username"
    DB_PASSWORD="your_password"
    DB_DATABASE="soengram"
   
   # Windows
   POST_UPLOAD_FOLDER = '\\static\\post_images\\'
    ```
6. Prep the db by running this command in the root of the project
   ```sh
   $ python3 ./seed/db_prep.py
   ```
7. Make the db migrations
   ```sh
   $ flask db upgrade
   ```
8. Seed test data
   ```sh
   $ python3 ./seed/seed.py
   ```
9. Start application
    ```sh
    $ flask run
    ```

### Running the Tests

Run all tests with the following command in the project virtual environment.

```
$ pytest
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) detailing basic guidlines for pushing new code to the repo and a basic workflow example.


## Acknowledgments

Soengram is an educational non-profitable project based on the social networking service [Instagram](https://instagram.com). The design and functionalities are adapted from Instagram to meet project requirements. This web application is not hosted for commercial use, but rather for academic purposes.

Copyright © 2021 Soengram adapted from Instagram and customized by Soengram team

### Libraries

This project uses the following libraries:
- [Infinite Scroll](https://infinite-scroll.com/), available under the [GNU GPL license v3](https://www.gnu.org/licenses/gpl-3.0.html) containing the following [notices and atrtibutions](https://infinite-scroll.com/license.html).

## Team

- Domenic Seccareccia [(@domsec)](https://github.com/domsec)
- Lea Lakkis [(@lea)](https://github.com/lealakkis)
- Jason Gerard [(@jason-gerard)](https://github.com/jason-gerard)
- Mahmoud Elsayed [(@mnashat)](https://github.com/mnashat)
- Fadi Albasha [(@fadi-albasha)](https://github.com/fadi-albasha)
- Lujain Khalaf [(@lujainkhalaf)](https://github.com/LujainKhalaf)
- David Lemme [(@David)](https://github.com/davrine)
