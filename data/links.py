from data.credentials import Credentials

class Links:
    user = Credentials.LOGIN_USER
    admin = Credentials.LOGIN_ADMIN

    HOST = "https://demo.opensource-socialnetwork.org"
    LOGIN_PAGE = f"{HOST}/login"
    NEWSFEED_PAGE = f"{HOST}/home"
    RESET_LOGIN_PAGE = f"{HOST}/resetlogin"
    USER_WALL_PAGE = f"{HOST}/u/GarryPotter"
    FRIENDS_PAGE = f"{HOST}/u/GarryPotter/friends"
    MESSAGES_ALL = f"{HOST}/messages/all"
    MESSAGE_USER_PAGE_IN_ADMIN_ACCOUNT = f"{HOST}/messages/message/GarryPotter"
    SEARCH_PAGE = f"{HOST}/search"
    NOTIFICATIONS_PAGE = f"{HOST}/notifications/all"


    FRIENDS_PAGE_USER = f"{HOST}/u/{user}/friends"
    FRIENDS_PAGE_ADMIN = f"{HOST}/u/{admin}/friends"
    USER_WALL_PAGE1 = f"{HOST}/u/{user}"
    ADMIN_WALL_PAGE = f"{HOST}/u/{admin}"



