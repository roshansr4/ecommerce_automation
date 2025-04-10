import configparser

config = configparser.RawConfigParser() #using raw configparser method and creating a config object
#by using config, we can actually read the config.ini file
config.read(".\\configurations\\config.ini") #providing the path of config.ini file inside the read method
#Now fetch the test data

class Read_Config:
#we'll write static method to fetch every variable from config.ini
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info', 'admin_page_url')
        return url
    #So whenever we call this get_admin_page_url method, it will return the url value from admin login info section
    #Do the same thing for other variables

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def get_invalid_username(): #Note to self: No need to provide 'self' parameter in static method
        invalid_username = config.get('admin login info', 'invalid_username')
        return invalid_username


