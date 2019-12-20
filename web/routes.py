from views import index, health, getwifiname

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/health', health)
    app.router.add_get('/getwifiname', getwifiname)


