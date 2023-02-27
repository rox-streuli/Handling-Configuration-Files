# Level of difficulty
# Easy
#
# Estimated time
# 30 minutes
#
# Objectives
# improving the student's skills in parsing configuration files;
# improving the student's skills in creating configuration files.

# Scenario
# Imagine a situation in which you receive a configuration file
# containing access data for various services. Unfortunately, the
# file is a terrible mess, because it contains data used in both
# production and development environments.
#
# Your task will be to create two files named prod_config.ini and
# dev_config.ini. The prod_config.ini file should only contain
# sections for the production environment, while dev_config.ini
# should only contain sections for the development environment.
#
# To distinguish between the environments, use the env option added
# to all sections in the mess.ini file. The env option should be
# removed from the sections before moving them to the files.
#
# Expected result
# The prod_config.ini file:
#
# [sentry]
# key = key
# secret = secret
#
# [github]
# user = user
# password = password
#
#
# The dev_config.ini file:
#
# [mariadb]
# host = localhost
# name = hello
# user = user
# password = password
#
# [redis]
# host = localhost
# port = 6379
# db = 0
#
# Use mess.ini file

import configparser


class MessConfigParser:
    def __init__(self):
        self.prod_sections = {}
        self.dev_sections = {}

    def parse(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)

        for section in config.sections():
            for key in config[section]:
                if key == 'env':
                    continue
                else:
                    dict_1 = {key: config[section][key]}

                    if config[section]['env'] == 'prod':
                        if section not in self.prod_sections:
                            self.prod_sections[section] = {}
                        self.prod_sections[section].update(dict_1)
                    else:
                        if section not in self.dev_sections:
                            self.dev_sections[section] = {}
                        self.dev_sections[section].update(dict_1)


class ConfigParserHelper:
    def write_from_dict(self, filename, dict_1):
        config = configparser.ConfigParser()
        config.read_dict(dict_1)

        with open(filename, 'w') as configfile:
            config.write(configfile)


mess_config_parser = MessConfigParser()
mess_config_parser.parse('mess.ini')

helper = ConfigParserHelper()
helper.write_from_dict('prod_config.ini', mess_config_parser.prod_sections)
helper.write_from_dict('dev_config.ini', mess_config_parser.dev_sections)


# IS MORE EFFICIENT IF WE USE...
# for section in config.sections():
#     if section.has_section(section, option):
# and filter sections from that result!!!
