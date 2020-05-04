Set:

```
VERSION=1.0.0
REPO_URL=paolamedo/numerical_methods
BUILD_DIR=/home/user/midir
```
Use:
```
docker pull $REPO_URL:$VERSION
```

Build:

```
docker build $(pwd) --force-rm -t $REPO_URL:$VERSION
```

Upload to Dockerhub:
```
docker login
docker push $REPO_URL:$VERSION
```


Run:

```
docker run --rm -it --name jupyterlab-local -p 8888:8888 -v $BUILD_DIR:/home/jovyan/work $REPO_URL:$VERSION
```




## jupyter lab running at localhost:8888

(not necessary) Enter to docker container with:

```
docker exec -it -u=miuser jupyterlab-local bash
```

Stop:

```
docker stop jupyterlab-local
```

Delete (if `--rm` wasn't used):


```
docker rm jupyterlab-local
```
