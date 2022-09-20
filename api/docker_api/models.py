from pydantic import BaseModel, Field
from typing import List


class DockerResponseModel(BaseModel):
    ErrorCode: int = 0
    Message: str = None


class DockerContainerLsResponseModelItems(BaseModel):
    ContainerID: str
    ContainerName: str
    Status: str
    Image: str
    CreatedAt: str
    RunningFor: str
    Ports: str = None
    Mounts: str = None


class DockerLsResponseModel(DockerResponseModel):
    Containers: list[DockerContainerLsResponseModelItems] = None


class DockerImageLsResponseModelItems(BaseModel):
    ContainerID: str
    CreatedSince: str
    ID: str
    Repository: str
    Tag: str
    CreatedAt: str
    Size: str = str


class DockerImageResponseModel(DockerResponseModel):
    Images: list[DockerImageLsResponseModelItems] = None


class DockerNetworkLsResponseModelItems(BaseModel):
    ID: str
    Name: str
    Driver: str
    Scope: str


class DockerNetworkResponseModel(DockerResponseModel):
    Networks: list[DockerNetworkLsResponseModelItems] = None


