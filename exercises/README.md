# Lesson 2
## Exercise Endpoints for Application Status and Logging

```bash
cd python-helloworld
#DEV
docker build --target dev  -t cff-endpoints:dev .
#PROD
docker build -t cff-endpoints:prod  .

# live coding
docker run --rm --name flask-endpoints -i -t -p 5000:5000 -v $(pwd):/app cff-endpoints:dev


# prod -> Use it with WSGI server
docker run --name flask-endpoints-prod -i -t -p 5000:5000 --restart always cff-endpoints:prod 

```

# Lesson 3
## 
```bash
cd go-helloworld

#Build
docker build -t turnes/go-helloworld

#Tag
docker tag turnes/go-helloworld turnes/go-helloworld:0.1.0

#Push
docker login
docker push turnes/go-helloworld:0.1.0

#RUN
docker run --rm --name helloworld -i -t -p 6111:6111 turnes/go-helloworld:0.1.0

```