# Build
Go to the docker folder and run:

```bash
$ docker build -t cursopython -f Dockerfile .
```

# How to
Run the following command:

```bash
$ docker run -d --rm --mount type=bind,src="$(pwd)",dst=/app --name curso cursopython
```
