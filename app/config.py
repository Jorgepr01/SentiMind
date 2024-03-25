class Config():
    SECRET_KEY = "B!1weNAt1T^%kvhUI*S^"
    # SECRET_KEY_FAKE = "B!1w8NAt1T^%kvhUI*S^"


class DevConfig(Config):
    DEBUG= True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'Santa'
    MYSQL_PASSWORD = '123'
    MYSQL_DB = 'sentimientos'


config={
    "development": DevConfig 
}