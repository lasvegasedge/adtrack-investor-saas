from flask import request, redirect
from werkzeug.middleware.proxy_fix import ProxyFix

app = create_app()

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

@app.before_request
def redirect_to_www():
    host = request.host.split(':')[0]
    print(f"🔹 Host header is: {request.host}")
    if host == 'adtrackpitch.online':
        target = f'https://www.adtrackpitch.online{request.full_path}'
        print(f"🌐 Redirecting from {request.host}{request.full_path} to {target}")
        return redirect(target, code=301)
