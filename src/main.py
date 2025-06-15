app = create_app()

@app.before_request
def redirect_to_www():
    host = request.host.split(':')[0]
    if host == 'adtrackpitch.online':
        print(f"🌐 Redirecting from {request.host}{request.full_path}")
        return redirect(f'https://www.adtrackpitch.online{request.full_path}', code=301)
