# Recruitment task Contelizer

This application was created as part of an application to the Contelizer

**Tech stack:**
 - Python 3.11
 - Django
 - Django Rest Framework
 - React


To run this application:

 - clone repository
 - from location when docker-compose file exists run:
 
  ```
  docker-compose up --build
  ```
  Application will be running on 

  ``` api - localhost:8000```

  ``` frontend - localhost:3000```

## Running Tests

To run tests, enter container with the following command

```bash
  docker exec -it contelizer_api sh
```

And run
```bash
  python manage.py test
```

