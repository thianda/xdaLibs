from xdaLibs import iniconfig

conf = iniconfig.IniConfig('config.ini')
print(conf.get('database', 'db'))
print(conf.get('database', 'password'))

# change password
conf.set('database', 'password','new_password')
print(conf.get('database', 'password'))

