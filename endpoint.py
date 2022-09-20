from fastapi import FastAPI
from api.docker_api.router import docker_wrapper
from api.docker_swarm_api.router import docker_swarm_wrapper
app = FastAPI(title='DockerWrapper',
              description='API Wrapper for docker',
              version='0.0.1', )


@app.get('/')
def health_check():
    return 'API is running'


app.include_router(docker_wrapper)
app.include_router(docker_swarm_wrapper)
