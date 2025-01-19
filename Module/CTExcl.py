# CTExcl.py
# Filter pairs out depending on given term inclusion.
# Jan-2025 @CelestialAddy

##### Functionality.

def Excl(Texts={}, Term="", CaseSensitive=True, TermSplitChar=">"):
    Ress = Texts.copy()
    St = list(Texts.keys())
    Tx = list(Texts.values())
    Type = Term.split(TermSplitChar)[0].upper()
    Text = ""
    for N in range(1, len(Term.split(TermSplitChar))):
        Text = Text + Term.split(TermSplitChar)[N]
        continue
    if Type == "XS":
        for S in St:
            if CaseSensitive == True:
                if S.find(Text) != -1: del Ress[S]
            if CaseSensitive == False:
                if S.upper().find(Text.upper()) != -1: del Ress[S]
            continue
    if Type == "XT":
        for T in Tx:
            if CaseSensitive == True:
                if T.find(Text) != -1:
                    del Ress[St[Tx.index(T)]]
                    Tx[Tx.index(T)] = None
            if CaseSensitive == False:
                if T.upper().find(Text.upper()) != -1:
                    del Ress[St[Tx.index(T)]]
                    Tx[Tx.index(T)] = None
            continue
    return Ress

# End.
