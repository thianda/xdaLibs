from xdaLibs import iniconfig

conf = iniconfig.IniConfig('tests/config.ini')
print(conf.get('database', 'db'))
