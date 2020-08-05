from sanic import Sanic
from sanic.response import json
from sanic_jwt import Initialize
from sanic_jwt import exceptions
from sanic_jwt.decorators import protected
from API.users import username_table
import json as js


async def authenticate(request, *args, **kwargs):
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    user = username_table.get(username, None)
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")

    if password != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user

app = Sanic(name="API")
Initialize(app, authenticate=authenticate)


# def return_normalize_item(item):
#     valueKey = {}
#     for key in list(item):
#         if "Val" in key:
#             valueKey = key
#     return {item["name"]: item[valueKey]}


@app.post("/normalize")
@protected()
async def test(request):
    body = js.loads(request.body)
    normalized = {item["name"]: item[key] for item in body for key in list(item) if "Val" in key}
    return json(normalized)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
