from src import create_app
from flask import request, redirect

app = create_app()

@app.before_request
def redirect_to_www():

    if request.host == 'adtrackpitch.online':
        return redirect(f'https://www.adtrackpitch.online{request.full_path}', code=301)

if __name__ == "__main__":
    app.run(debug=True)
