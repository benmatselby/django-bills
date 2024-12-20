# Django bills

A little app to store household bills in MySQL with a Django application.

A place to learn.

## Installation

Pre-requisites:

- [Docker](https://www.docker.com/) to run MySQL
- [uv](https://docs.astral.sh/uv/)
- [Python 3.13.+](https://www.python.org)

Then you can run:

```shell
make install bootstrap
```

This will install Python for you, the project dependencies, and run MySQL in docker.

## Running the dev server

We can now run the application.

```shell
make dependencies-run run
```

## To do

- Hook up to GitHub Actions
- Add some tests so need MySQL running in GHA
