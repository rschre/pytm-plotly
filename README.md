# pytm-skeleton

This repository contains a skeleton to create a new exercise for the _Python Tool Manager_.
You can find more information on the _Python Tool Manager_ in the
corresponding [documentation on GitHub](https://ofabel.github.io/pytm-bootstrap/).

## Usage

First, you need to create a
new [GitHub repository from this template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
and clone the just created repository on your computer.

### Create a Virtual Python Environment

Open a terminal window, navigate to the cloned or downloaded repository folder and execute the following command:

```shell
python -m venv venv
```

This will create a new `venv` folder, containing the virtual environment. It's mandatory, that folder's name is `venv`.

### Install the Dependencies

Open a terminal window, navigate to the cloned or downloaded repository
folder, [activate the virtual environment](https://docs.python.org/3/library/venv.html#how-venvs-work) and execute the
following command:

```shell
pip install -r requirements.txt
```

### Run an Exercise

To run an exercise you need to open a terminal window, navigate to the cloned or downloaded repository folder and
activate the virtual environment. Now, navigate to the desired exercise folder and execute the following command:

```shell
flask run --debug
```

## Things Left To Do

* [ ] Change this [Readme.md](./README.md) file according to your project.
* [ ] Change the [license](./LICENSE) according to your needs.
* [ ] Add your additional requirements to the [requirements.txt](requirements.txt) file.
* [ ] Keep the [changelog](./CHANGELOG.md) up to date. 
