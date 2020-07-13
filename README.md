# fibonacci-Restful-webservice
A repository to use REST web service to display Fibonacci sequence


## To build the docker container
```docker build -t fib-restful-web .```

## To run the docker container
```docker run -p 0.0.0.0:80:8080/tcp fib-restful-web```
This exposes port 80 on 0.0.0.0

## To use the RESTful web service
*Head to 0.0.0.0:80*

## The webpage should show:
![alt text](https://github.com/chadgavin/fibonacci-Restful-webservice/image.png)

## Follow the instructions ont the site and
insert */fibonacci/number* to the end of  *0.0.0.0:80* 

## To stop docker container 
```docker stop``` container_id
