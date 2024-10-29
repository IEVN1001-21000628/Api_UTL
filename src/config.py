class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST='localhost:3306'
    MYSQL_USER='root' 
    MYSQL_PASSWORD=''
    MYSQL_DB='api_utl'

config={
    'development':DevelopmentConfig
}