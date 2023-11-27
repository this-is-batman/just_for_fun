# Repositories for some random code snippets

This repository contains the code snippets, which I write for fun, when inspiration strikes, or when I am getting too bored. The structure is not too complicated, and mostly contains only script files in python. 

## Directory structure
* All the python scripts are present in the `/src/` directory.
* All the test functions , including the pytest modules are present in the `/tests` directory.


## For storing the nltk data
* All the nltk data is stored inside `~/home/user_name/nltk_data/`.
* Download the packages required using the following lines of code for nltk
```
import nltk
nltk.download({package_name}, download_dir = '~/home/user_name/nltk_data/')
```

## Added CI/CD workflow through Github actions
Added CI/CD integration with Github using Github Actions. The github actions workflow is defined in the file `.github/workflows/build.yml`. Further improvements will be made to the workflow file in future iterations.

**Future**: In future, or whenever I wish, I also wish to write some codes in C++ or in C, and store it in github for posterity.

**Disclaimer**: For now, this is meant to be a private repository. At any point in the future though, it may be made public according to my wishes.

## Added dockerfile

Added a `Dockerfile` which contained instructions about creating a docker image, and a docker container to run the scripts in this repository. Doing this to get used to `containerization` and deploying applications inside a container. 

We can use the following commands to use this Dockerfile - 

```
docker build -t {name_of_the_image} .
```
The above command will be used to create an image.

To create a `container` from that image, we will use the following command - 

```
docker run -it --rm just_for_fun_img
```

The above command will spawn a container from that image and then delete the container on succesful completion.

Go to this [link](https://docs.docker.com/engine/reference/commandline/cli/) to learn more about Docker CLI.