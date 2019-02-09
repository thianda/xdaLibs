from xdaLibs import iniconfig

conf = iniconfig.IniConfig('config.ini')
print(conf.get('database', 'db'))
