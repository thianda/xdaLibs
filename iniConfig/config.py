#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser


class Config(object):
    def __init__(self, file):
        self.file = file
        self.config = configparser.ConfigParser()
        self.config.read(file)

    def get(self, section, option):
        """
        获取值
        """
        self.checkOption(section, option)
        value = self.config.get(section, option)
        return value

    def listOptions(self, section):
        """
        返回指定 section 的全部 option 值的数组形式
        """
        self.checkSection(section)
        return [self.config[section][x] for x in self.config.options(section)]

    def checkSection(self, section):
        """
        检查指定的 section 是否存在
        """
        if section not in self.config:
            print('Nothing named ' + section + ' in file: ' + self.file)
            return None

    def checkOption(self, section, option):
        """
        检查指定的 section 中的 option 是否存在
        """
        self.checkSection(section)
        if option not in self.config[section]:
            print('There\'s no option named ' + option +
                  ' for ' + section + ' in file: ' + self.file)