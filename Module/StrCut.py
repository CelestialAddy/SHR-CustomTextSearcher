# StrCut.py
# Cut-off a string if above a given length.
# Jan-2025 @CelestialAddy

##### Functionality.

def Fade(Str="", Len=0, Sig="[...]"):
    if len(str(Str)) >= int(Len):
        Str = str(Str)[0:int(Len)] + str(Sig)
    return str(Str)

# End.
