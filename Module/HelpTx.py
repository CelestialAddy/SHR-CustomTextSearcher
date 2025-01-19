# HelpTx.py
# Help messages and print function.
# Jan-2025 @CelestialAddy

##### Definitions.

U_HELPERS = [
    " USAGE (op names case-insensitive):",
    "\ts|...    : Limit results pool to Strings containing \"...\".",
    "\tt|...    : Limit results pool to Texts containing \"...\".",
    "\txs|...   : Limit results pool to Strings not containing \"...\".",
    "\txt|...   : Limit results pool to Texts not containing \"...\".",
    "\tL        : Load whole textbible to results pool (asked for path and encoding).",
    "\tS        : Save current results pool to text file (asked for path and encoding).",
    "\tC        : Toggle case-sensitive mode for s/t/xs/xt operations.",
    "\tR        : Restore results pool to state upon last L operation.",
    "\tN        : State results pool size.",
    "\tPAD      : Toggle padding String-Text pairs for alignment when listing results pool pairs.",
    "\tCUT      : Toggle fading long Texts when listing results pool pairs.",
    "\tX        : Exit program.",
    "\tHELP     : Show usage information.",
    " String=Text",
    " You almost certainly want either \"UTF-8\" (mod) or \"UTF-16\" (vanilla) for encodings.",
    " PAD and CUT states do not affect S operation output, only results pool listings in UI.",
    " CLI users can do \"python -m CTSearcher.py <path> <encoding>\" or similar as a shortcut.",
    ]

##### Functionality.

def Help():
    for Ln in U_HELPERS:
        print(str(Ln))
        continue
    return None

# End.
