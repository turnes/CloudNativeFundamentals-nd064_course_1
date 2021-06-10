# Lesson 2
## Exercise Endpoints for Application Status

```bash

#DEV
docker build --target dev  -t cff-endpoints:dev .
#PROD
docker build -t cff-endpoints:prod  .

# live coding
docker run --rm --name flask-endpoints -i -t -p 5000:5000 -v $(pwd):/app cff-endpoints:dev


# prod -> Use it with WSGI server
docker run --name flask-endpoints-prod -i -t -p 5000:5000 --restart always cff-endpoints:prod 

```


format='%(asctime)s, %(message)s endpoint was reached.', datefmt="%m/%d/%Y %I:%M:%S %p %Z")
