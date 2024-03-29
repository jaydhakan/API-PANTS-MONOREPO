import uvicorn
from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app_config import ENVIRONMENT, HOST, PORT
from apps.auth.src.route import auth_route
from apps.platform.src.modules.posts.route import posts_route
from apps.platform.src.modules.users.route import users_route
from libs.utils.common.src.modules.environments import is_internal_environment
from libs.utils.limiter.src.helpers import limiter

is_internal_env = is_internal_environment(ENVIRONMENT)

app = FastAPI(
    title='Application: MAIN',
    version='0.0.2',
    docs_url='/docs' if is_internal_env else None,
    redoc_url='/redoc' if is_internal_env else None,
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(auth_route)
app.include_router(users_route)
app.include_router(posts_route)

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host=HOST,
        port=PORT,
        reload=ENVIRONMENT
    )
