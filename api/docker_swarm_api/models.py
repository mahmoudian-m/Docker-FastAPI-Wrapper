from pydantic import BaseModel, Field
from typing import List


class DockerResponseModel(BaseModel):
    ErrorCode: int = 0
    Message: str = None


class DockerNodeLsResponseModelItems(BaseModel):
    ID: str
    Hostname: str
    Availability: str
    ManagerStatus: str
    EngineVersion: str
    Status: str


class DockerNodeResponseModel(DockerResponseModel):
    Nodes: list[DockerNodeLsResponseModelItems] = None


class DockerServiceLsResponseModelItems(BaseModel):
    ID: str
    Name: str
    Image: str
    Mode: str
    Ports: str
    Replicas: str


class DockerServiceLsResponseModel(DockerResponseModel):
    Services: list[DockerServiceLsResponseModelItems] = None


class DockerServicePsResponseModelItems(BaseModel):
    CurrentState: str
    DesiredState: str
    Error: str
    ID: str
    Image: str
    Name: str
    Node: str
    Ports: str


class DockerServicePsResponseModel(DockerResponseModel):
    ServicesPs: list[DockerServicePsResponseModelItems] = None


class DockerServiceLogsResponseModel(DockerResponseModel):
    ServiceLogs: str = None


class DockerServiceRMRequestModel(BaseModel):
    ServiceName: str = None


class DockerServiceRMResponseModel(DockerResponseModel):
    ServiceName: str = None
