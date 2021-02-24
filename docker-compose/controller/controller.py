import kopf


@kopf.on.login()
async def login_fn(**kwargs):
    return kopf.ConnectionInfo(
        server='http://apiserver:8080',
        insecure=True,
    )

@kopf.on.create('kopfexamples')
def create_fn(spec, **kwargs):
    print(f"And here we are! Creating: {spec}")
    return {'message': 'hello world'}  # will be the new status
