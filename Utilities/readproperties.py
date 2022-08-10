import configparser


config = configparser.RawConfigParser()
config.read("D:\\Automation_Program\\phython\\program\\Keyword_Frame_work\\facebook\\configuration\\config.properties")


class Read_config:
    @staticmethod
    def get_url():
        url = config.get("common info", "url")
        return url
    @staticmethod
    def get_username():
        username = config.get("commom info", "username")
        return username
    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password

