from waifuai import waifuai


def say(X_RAPIDAPI_KEY: str, user_id: str = "", message: str = ""):
    return waifuai.get_response(X_RAPIDAPI_KEY=X_RAPIDAPI_KEY, user_id=user_id, message=message)
