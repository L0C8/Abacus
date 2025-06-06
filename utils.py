import os, configparser

REQUIRED_DIRS = ["data", "cache"]
REQUIRED_DATA = ["themes"]

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

def create_ini_theme():
    config = configparser.ConfigParser()

    config["light"] = {
        "col_bg": "255,255,255",
        "col_f0": "0,0,0",
        "col_f1": "60,60,60",
        "col_f2": "120,120,120",
        "col_bc": "200,200,200",
        "col_mu": "0,128,0",      
        "col_md": "200,0,0"       
    }

    config["dark"] = {
        "col_bg": "30,30,30",
        "col_f0": "255,255,255",
        "col_f1": "200,200,200",
        "col_f2": "150,150,150",
        "col_bc": "90,90,90",
        "col_mu": "0,255,0",      
        "col_md": "255,60,60"     
    }

    path = os.path.join("data", "themes.ini")
    with open(path, "w") as configfile:
        config.write(configfile)

def validate_themes():
    """
    Validate that each theme in 'themes.ini':
    - Has exactly 7 expected color keys
    - Each color is a valid RGB string (3 integers, 0–255)
    """
    path = os.path.join("data", "themes.ini")

    if not os.path.exists(path):
        print("themes.ini not found.")
        return False

    config = configparser.ConfigParser()
    config.read(path)

    expected_keys = {"col_bg", "col_f0", "col_f1", "col_f2", "col_bc", "col_mu", "col_md"}

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
            print(f"Invalid theme '{section}': incorrect keys. Missing or extra: {keys ^ expected_keys}")
            all_valid = False
            continue

        for key in expected_keys:
            value = config[section][key]
            if not is_valid_rgb(value):
                print(f"Invalid RGB value in theme '{section}', key '{key}': '{value}'")
                all_valid = False

    if all_valid:
        print("Valid themes.")
    else:
        print("Invalid themes found.")

    return all_valid
