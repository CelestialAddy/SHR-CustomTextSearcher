# CTFind.py
# Filter pairs in depending on given term inclusion.
# Jan-2025 @CelestialAddy

##### Functionality.

def Find(Texts={}, Term="", CaseSensitive=True, TermSplitChar=">"):
    Ress = {}
    St = list(Texts.keys())
    Tx = list(Texts.values())
    Type = Term.split(TermSplitChar)[0].upper()
    Text = ""
    for N in range(1, len(Term.split(TermSplitChar))):
        Text = Text + Term.split(TermSplitChar)[N]
        continue
    if Type == "S":
        for S in St:
            if CaseSensitive == True:
                if S.find(Text) != -1: Ress[S] = Tx[St.index(S)]
            if CaseSensitive == False:
                if S.upper().find(Text.upper()) != -1: Ress[S] = Tx[St.index(S)]
            continue
    if Type == "T":
        for T in Tx:
            if CaseSensitive == True:
                if T.find(Text) != -1:
                    Ress[St[Tx.index(T)]] = T
                    Tx[Tx.index(T)] = None
            if CaseSensitive == False:
                if T.upper().find(Text.upper()) != -1:
                    Ress[St[Tx.index(T)]] = T
                    Tx[Tx.index(T)] = None
            continue
    return Ress

# End.
