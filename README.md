# machine-learning-project
 ML project 1


````
creating conda environment
a
conda create -p venv python==3.7 -y
```
actvate conda environment venv

conda activate venv/

````

pip install -r requirements.txt
```

To add file to git
```
git add .
```

OR
```
git add  <file_name>
```


> NOTE: To load file or folde from git we can write name of file or folder in .gitignore file

To check the git status 
```
git status
```

To check all version made by git 
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```
To send changes/version to github
```
git push origin main
```

To check remote url
```
git remote -v
```
HEROKU_EMAIL =aalen.ai3868@gmail.com
HEROKU_API_KEY =<>
HEROKU_APP_NAME =ml-regression-2


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
>Note: image name for docker must be in lowercase
```


To list docker images
```
Docker images
````

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 2b7a28ee36ed
```


To check running containers
````
docker ps
```

To stop a container
```
docker stop <container_id>
```