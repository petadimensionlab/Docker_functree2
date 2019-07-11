# Docker_functree2
docker functree2

Reference URL:https://bioviz.tokyo/functree2/

## 1.Usage
#### docker pull image

```
docker pull petadimensionlab/docker_functree2
```

#### docker run

```
docker run -it --name container_name -v /yourlocal_dir:/condir --rm  petadimensionlab/docker_functree2
```
Copy your "profile.tsv" into "/yourlocal_dir" 
example "profile.tsv"data =  https://bioviz.tokyo/functree2/static/data/example/profile.tsv

#### run python into this docker
```
/ # python3 tmp/functree2_docker.py
```
Execution result is output to "/yourlocal_dir"
