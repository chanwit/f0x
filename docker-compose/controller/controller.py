import kopf

@kopf.on.login()
async def login_fn(**kwargs):
    return kopf.ConnectionInfo(
        server='http://apiserver:8080',
        insecure=True,
    )

@kopf.on.create('compose')
def create(spec, **kwargs):
    print(f"And here we are! Creating: {spec}")
    return {'message': "version: {version}".format(version=spec["version"])}  # will be the new status
