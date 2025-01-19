# CTSearcher.py
# Console UI and core program loop.
# Jan-2025 @CelestialAddy

##### Requirements.

try:
    import Module.CTDump as Dumper
    import Module.CTExcl as Filter
    import Module.CTFind as Finder
    import Module.HelpTx as Helper
    import Module.OutRes as Storer
    import Module.StrCut as Cutter
    import Module.StrPad as Padder
except:
    input("(!) Unable to load required sub-modules from \"Module\" directory.\n")
    exit(0)

##### Definitions.

PROGRAM_V = "1"
CORE_LOOP = True
LOCK_CASE = True
PRINT_PAD = True
PRINT_CUT = True
PAD_THOLD = 65
TERM_CHAR = "|"
ALL_TEXTS = {}
U_ACTIONS = ""
TEMP_ASKS = [0,0,0,0,0]
U_RESULTS = {}

##### Program.

# A tiny splash of CLI functionality, for shortcut/convenience if nothing else.

try:
    import sys
    U_RESULTS = Dumper.Dump(Path=sys.argv[1], Codec=sys.argv[2])
    ALL_TEXTS = U_RESULTS.copy()
except:
    pass

print(f"CustomText Searcher (revision {PROGRAM_V}) by CelestialAddy\n" + "=" * 100)

while CORE_LOOP == True:
    U_ACTIONS = input("? ")
    if U_ACTIONS.upper().strip() == "HELP":
        Helper.Help()
    elif U_ACTIONS.upper().strip() == "L":
        TEMP_ASKS[0] = input("Path? ")
        TEMP_ASKS[1] = input("Encoding? ")
        try:
            U_RESULTS = Dumper.Dump(Path=TEMP_ASKS[0], Codec=TEMP_ASKS[1])
            ALL_TEXTS = U_RESULTS.copy()
            print(f"> Loaded textbible ({len(U_RESULTS.keys())} pairs).")
        except:
            print("(!) Operation failure.")
        TEMP_ASKS = [0,0,0,0,0]
    elif U_ACTIONS.upper().strip() == "S":
        TEMP_ASKS[0] = input("Path? ")
        TEMP_ASKS[1] = input("Encoding? ")
        try:
            Storer.Oupt(Texts=U_RESULTS, Path=TEMP_ASKS[0], Codec=TEMP_ASKS[1])
            print(f"> Output results ({len(U_RESULTS.keys())} pairs).")
        except:
            print("(!) Operation failure.")
        TEMP_ASKS = [0,0,0,0,0]
    elif U_ACTIONS.upper().strip() == "C":
        if LOCK_CASE == True:
            LOCK_CASE = False
            print("> Case-sensitivity OFF.")
        else:
             LOCK_CASE = True
             print("> Case-sensitivity ON.")
    elif U_ACTIONS.upper().strip() == "R":
        U_RESULTS = ALL_TEXTS.copy()
        print("> Restored textbible fully.")
    elif U_ACTIONS.upper().strip() == "N":
        print(f"({len(U_RESULTS.keys())} pairs.)")
    elif U_ACTIONS.upper().strip() == "PAD":
        if PRINT_PAD == True:
            PRINT_PAD = False
            print("> Print padding OFF.")
        else:
            PRINT_PAD = True
            print("> Print padding ON.")
    elif U_ACTIONS.upper().strip() == "CUT":
        if PRINT_CUT == True:
            PRINT_CUT = False
            print("> Print fading OFF.")
        else:
            PRINT_CUT = True
            print("> Print fading ON.")
    elif U_ACTIONS.upper().strip() == "X":
        exit(0)
    else:
        if (U_ACTIONS.lower().find("xs" + TERM_CHAR) != -1) or (U_ACTIONS.lower().find("xt" + TERM_CHAR) != -1):
            try:
                U_RESULTS = Filter.Excl(Texts=U_RESULTS, Term=U_ACTIONS, CaseSensitive=LOCK_CASE, TermSplitChar=TERM_CHAR)
                print(f"> Excluded term ({len(U_RESULTS.keys())} matches).")
                TEMP_ASKS[0] = 0
                for Str, Txt in U_RESULTS.items():
                    if len(Str) > TEMP_ASKS[0]:
                        TEMP_ASKS[0] = len(Str)
                    continue
                for Str, Txt in U_RESULTS.items():
                    if PRINT_PAD == True:
                        Str = Padder.RPad(Str=Str, Len=TEMP_ASKS[0] + 2, Chr=" ")
                    else:
                        Str = Str + " " + Txt
                    if PRINT_CUT == True:
                        Txt = Cutter.Fade(Str=Txt, Len=PAD_THOLD, Sig="[...]")
                    print(Str + Txt)
            except:
                print("(!) Operation failure.")
        elif (U_ACTIONS.lower().find("s" + TERM_CHAR) != -1) or (U_ACTIONS.lower().find("t" + TERM_CHAR) != -1):
            try:
                U_RESULTS = Finder.Find(Texts=U_RESULTS, Term=U_ACTIONS, CaseSensitive=LOCK_CASE, TermSplitChar=TERM_CHAR)
                print(f"> Ran search ({len(U_RESULTS.keys())} matches).")
                TEMP_ASKS[0] = 0
                for Str, Txt in U_RESULTS.items():
                    if len(Str) > TEMP_ASKS[0]:
                        TEMP_ASKS[0] = len(Str)
                    continue
                for Str, Txt in U_RESULTS.items():
                    if PRINT_PAD == True:
                        Str = Padder.RPad(Str=Str, Len=TEMP_ASKS[0] + 2, Chr=" ")
                    else:
                        Str = Str + " " + Txt
                    if PRINT_CUT == True:
                        Txt = Cutter.Fade(Str=Txt, Len=PAD_THOLD, Sig="[...]")
                    print(Str + Txt)
            except:
                print("(!) Operation failure.")
        TEMP_ASKS = [0,0,0,0,0]
    pass

input("(!) Core program loop escaped.\n")
exit(0)

# End.
