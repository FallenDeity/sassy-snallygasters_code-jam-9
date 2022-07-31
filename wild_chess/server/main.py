"""main server file"""

import fastapi
import uvicorn

from .routes import authentication, leaderboard, multiplayer

app = fastapi.FastAPI()

app.include_router(authentication.route)
app.include_router(leaderboard.route)
app.include_router(multiplayer.route)


def main() -> None:
    """Driver code."""
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
