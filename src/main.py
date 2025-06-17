from flask import Flask, request, redirect, render_template
from src import create_app

app = create_app()

@app.before_request
def redirect_to_www():
    host = request.host.split(':')[0]
    if host == 'adtrackpitch.online':
        print(f"🌐 Redirecting from {request.host}{request.full_path}")
        target = f"https://www.adtrackpitch.online{request.full_path}"
        return redirect(target, code=301)

@app.route("/")
def homepage():
    return render_template("main/index.html")  # 👈 Load your dynamic homepage here
