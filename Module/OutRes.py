# OutRes.py
# Output results to plain-text ".txt" file.
# Jan-2025 @CelestialAddy

##### Functionality.

def Oupt(Texts={}, Path="", Codec=""):
    Text = ""
    for Str, Txt in Texts.items():
        Text = Text + str(Str) + "=" + str(Txt) + "\n"
        continue
    Out = open(str(Path), "wt", encoding=str(Codec).lower())
    Out.write(Text)
    Out.close()
    return None

# End.
