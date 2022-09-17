from pydantic import BaseModel, Field
from typing import List


class DockerContainerLsResponseModelItems(BaseModel):
    ContainerID: str
    ContainerName: str
    Status: str
    Image: str
    CreatedAt: str
    RunningFor: str
    Ports: str = None
    Mounts: str = None


class DockerLsResponseModel(BaseModel):
    ErrorCode: int = 0
    Message: str = None
    Containers: list[DockerContainerLsResponseModelItems] = None
