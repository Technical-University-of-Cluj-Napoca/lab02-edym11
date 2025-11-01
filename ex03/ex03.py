import datetime
import os
def prBlue(s): print("\033[94m {}\033[00m".format(s), end = "")
def prRed(s): print("\033[91m {}\033[00m".format(s), end = "")
def prGray(s): print("\033[90m {}\033[00m".format(s), end = "")
def prYellow(s): print("\033[93m {}\033[00m".format(s), end = "")

def smart_log(*args, **kwargs) -> None:
    level = ""
    ts = True
    dt = False
    savet = False
    save_loc = ""
    color = True
    for k, val in kwargs.items():
        if k == "Level":
            level = val
        elif k == "timestamp":
            ts = val
        elif k == "date":
            dt = val
        elif k == "save_to":
            savet = True
            save_loc = val
        elif k == "color":
            color = val

    if color == True:
        if level == "info":
            if dt == True:
                x = datetime.datetime.now()
                prBlue(x.strftime("%d/%m/%Y"))  
            if ts == True:
                x = datetime.datetime.now()
                prBlue(x.strftime("%H:%M:%S"))
            prBlue(f"[{level.upper()}]")
            stri = "" 
            for i in args:
                stri = stri + i + " "
            prBlue(stri)
            print(" ")
        elif level == "debug":
            if dt == True:
                x = datetime.datetime.now()
                prGray(x.strftime("%d/%m/%Y"))  
            if ts == True:
                x = datetime.datetime.now()
                prGray(x.strftime("%H:%M:%S"))
            prGray(f"[{level.upper()}]")
            stri = "" 
            for i in args:
                stri = stri + i + " "
            prGray(stri)
            print(" ")
        elif level == "warning":
            if dt == True:
                x = datetime.datetime.now()
                prYellow(x.strftime("%d/%m/%Y"))  
            if ts == True:
                x = datetime.datetime.now()
                prYellow(x.strftime("%H:%M:%S"))
            prYellow(f"[{level.upper()}]")
            stri = "" 
            for i in args:
                stri = stri + i + " "
            prYellow(stri)
            print(" ")
        elif level == "error":
            if dt == True:
                x = datetime.datetime.now()
                prRed(x.strftime("%d/%m/%Y"))  
            if ts == True:
                x = datetime.datetime.now()
                prRed(x.strftime("%H:%M:%S"))
            prRed(f"[{level.upper()}]")
            stri = "" 
            for i in args:
                stri = stri + i + " "
            prRed(stri)
            print(" ")
    else:
        if dt == True:
            x = datetime.datetime.now()
            print(x.strftime("%d/%m/%Y"), end = " ")  
        if ts == True:
            x = datetime.datetime.now()
            print(x.strftime("%H:%M:%S"), end = " ")
        print(f"[{level.upper()}]", end = " ")
        stri = "" 
        for i in args:
            stri = stri + i + " "
        print(stri, end = " ")
    
    if savet == True and save_loc:
        parts = []
        x = datetime.datetime.now()
        if dt:
            parts.append(x.strftime("%d/%m/%Y"))
        if ts:
            parts.append(x.strftime("%H:%M:%S"))
        parts.append(f"[{level.upper()}]")
        stri = "" 
        for i in args:
            stri = stri + i + " "
        parts.append(stri)

        log_l = ""
        for i in parts:
            log_l = log_l + i + " "
        os.makedirs(os.path.dirname(save_loc), exist_ok = True)
        with open(save_loc, "a") as f:
            f.write(log_l + "\n")


if __name__ == "__main__":
    username = "Vro"
    smart_log("System started successfully.", Level = "info", timestamp = True, date = True, save_to = "logs/system.log", color = True)
    smart_log("User", username, "logged in", Level = "debug", timestamp = True)
    smart_log("Low disk space detected!", Level = "warning", save_to = "logs/system.log")
    smart_log("Model", "Training", "failed!", Level = "error", color = True, save_to = "logs/system.log")
    smart_log("Process end", Level = "info", color = False, save_to = "logs/system.log")
    pass