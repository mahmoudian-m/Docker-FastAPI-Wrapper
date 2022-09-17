from fastapi import FastAPI

app = FastAPI(title='DockerWrapper',
              description='API Wrapper for docker',
              version='0.0.1', )


@app.get('/')
def health_check():
    return 'API is running'
