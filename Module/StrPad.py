# StrPad.py
# Pad a string on either side (given character/length).
# Jan-2025 @CelestialAddy

##### Functionality

def RPad(Str="", Len=0, Chr=" "):
    while len(str(Str)) < int(Len):
        Str = str(Str) + str(Chr)
    return str(Str)

def LPad(Str="", Len=0, Chr=" "):
    while len(str(Str)) < int(Len):
        Str = str(Chr) + str(Str)
    return str(Str)

# End.
