from configparser import ConfigParser, SectionProxy


cfg = ConfigParser()
fp = 'gameconfig.ini'
cfg.read(fp)
# print(cfg.read(fp))

# ToDo Initialisatie fase????
# code


def write_to_file(mode='w'):
    """
    r = reading
    w = writing
    a = appending
    r+ = both reading and writing
    """
    with open(fp, mode) as configfile:
        cfg.write(configfile)


### Sections ###
def config_create_section(section_name: str) -> None:
    cfg.add_section(section_name)
    write_to_file()


def config_get_section(section_name: str) -> SectionProxy:
    return cfg[section_name]


def config_get_all_sections() -> list:
    return cfg.sections()


def config_set_section(old_name, new_name):
    # Store options interal
    options = dict(cfg.items(old_name))
    # remove whole section
    cfg.remove_section(old_name)
    # create new section
    cfg.add_section(new_name)
    # add stored options to new section
    for option in options:
        cfg[new_name][option] = options[option]
    # write to file
    write_to_file()

def config_remove_section(section):
    cfg.remove_section(section)
    write_to_file()


### Items ###
def config_create_item(section, optionkey, optionval):
    cfg[section][optionkey] = optionval
    write_to_file()


def config_get_item(section, name):
    return cfg.get(section, name)


def config_set_item(section, optionkey, optionval):
    config_create_item(section, optionkey, optionval)
    write_to_file()


def config_remove_item(section, option):
    cfg.remove_option(section, option)
    write_to_file()

if __name__ == '__main__':
    print(config_get_all_sections())