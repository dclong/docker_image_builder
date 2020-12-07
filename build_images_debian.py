#!/usr/bin/env python3
import dsutil.docker

images = [
    "https://github.com/dclong/docker-jupyterhub-ds.git",
    "https://github.com/dclong/docker-vscode-server.git",
    "https://github.com/dclong/docker-rustpython.git",
]
builder = dsutil.docker.DockerImageBuilder(images, branch="debian")
builder.build()
