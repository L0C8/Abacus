import os, configparser

REQUIRED_DIRS = ["data", "cache"]
REQUIRED_DATA = ["settings", "themes"]

def boot_check():
    for folder in REQUIRED_DIRS:
        check_dir(folder)
    for ini_name in REQUIRED_DATA:
        check_ini(ini_name)
    validate_themes()

def check_dir(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def check_ini(file_name):
    path = os.path.join("data", f"{file_name}.ini")
    if not os.path.exists(path):
        if(file_name == "themes"):
            create_ini_theme()
        if(file_name == "settings"):
            create_ini_settings()

def create_ini_settings():
    config = configparser.ConfigParser()
    config["App"] = {
        "theme": "dark"
    }

    path = os.path.join("data", "settings.ini")
    with open(path, "w") as configfile:
        config.write(configfile)

    print(f"Default settings written to {path}")

def create_ini_theme():
    config = configparser.ConfigParser()

    config["dark"] = {
        "col_bg": "30,30,30",
        "col_f0": "255,255,255",
        "col_f1": "200,200,200",
        "col_f2": "150,150,150",
        "col_bc": "90,90,90",
        "col_b1": "40,40,40",
        "col_b2": "60,60,60",
        "col_b3": "40,40,40",
        "col_mu": "0,255,0",
        "col_md": "255,50,50"
    }

    config["light"] = {
        "col_bg": "255,255,255",
        "col_f0": "0,0,0",
        "col_f1": "60,60,60",
        "col_f2": "120,120,120",
        "col_bc": "200,200,200",
        "col_b1": "180,180,180",
        "col_b2": "230,230,230",
        "col_b3": "180,180,180",
        "col_mu": "0,128,0",
        "col_md": "200,0,0"
    }

    config["darksky"] = {
        "col_bg": "25,30,45",
        "col_f0": "220,230,255",
        "col_f1": "170,190,220",
        "col_f2": "120,140,180",
        "col_bc": "80,90,110",
        "col_b1": "30,40,60",
        "col_b2": "50,60,80",
        "col_b3": "30,40,60",
        "col_mu": "100,255,200",
        "col_md": "255,80,80"
    }

    path = os.path.join("data", "themes.ini")
    with open(path, "w") as configfile:
        config.write(configfile)

def validate_themes():
    path = os.path.join("data", "themes.ini")
    if not os.path.exists(path):
        print("themes.ini not found.")
        return False

    config = configparser.ConfigParser()
    config.read(path)

    expected_keys = {
        "col_bg", "col_f0", "col_f1", "col_f2",
        "col_bc", "col_b1", "col_b2", "col_b3",
        "col_mu", "col_md"
    }

    def is_valid_rgb(value):
        try:
            parts = [int(p.strip()) for p in value.split(",")]
            return len(parts) == 3 and all(0 <= p <= 255 for p in parts)
        except ValueError:
            return False

    all_valid = True
    for section in config.sections():
        keys = set(config[section].keys())
        if keys != expected_keys:
            print(f"Invalid theme '{section}': key mismatch. Missing or extra keys: {keys ^ expected_keys}")
            all_valid = False
            continue

        for key in expected_keys:
            value = config[section][key]
            if not is_valid_rgb(value):
                print(f"Invalid RGB in theme '{section}', key '{key}': '{value}'")
                all_valid = False

    if all_valid:
        print("Valid themes.")
    else:
        print("Invalid themes found.")

    return all_valid

def get_available_themes():
    path = os.path.join("data", "themes.ini")
    config = configparser.ConfigParser()
    config.read(path)
    return config.sections()

def set_theme(theme_name):
    path = os.path.join("data", "settings.ini")
    config = configparser.ConfigParser()
    config.read(path)

    if "App" not in config:
        config["App"] = {}

    config["App"]["theme"] = theme_name

    with open(path, "w") as configfile:
        config.write(configfile)

    print(f"Theme set to '{theme_name}'")
