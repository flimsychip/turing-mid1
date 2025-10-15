# WCBC libraries
from universal import universal
import utils
from utils import rf

# Oracle function  -- assume it exists to prove 
# by contradiction that it cannot possibly exist
from lastSymbol import lastSymbol  

def altersYesToLastSymbol(inString):
    #** Midterm #1: Add code needed before the call to universal()
    (progString, viaInString) = utils.DESS(inString)
    # progString == 1st arg to yesViaLastSymbol
    # viaInString == 2nd arg to yesViaLastSymbol
    result = universal(progString, viaInString)
    #** Midterm #1: Add code needed after the call to universal()
    if result == 'yes':
        if len(inString) >= 1:
            return inString[-1]
        else:
            return ''
    else:
        return 'anything that is neither the last character nor empty if input is empty. this should be ok since it is longer than one char'

def yesViaLastSymbol(progString,inString):
    #** Midterm #1: Add code needed before call to lastSymbol()
    singleString = utils.ESS(progString, inString)
    #** Midterm #1: Add 2nd arg to LastSymbol call, if needed.
    #** If not needed, erase ', . . .'
    val = lastSymbol(rf('altersYesToLastSymbol.py'), singleString)
    #** Midterm #1: Add code needed after call to LastSymbol()
    return val

'''
Midterm #1: Explain why the Python code above proves that LastSymbol is undecidable.
we assume lastSymbol() exists and can always decide whether a program correctly outputs the last symbol of an input. if it exists,
we can write a program altersYesToLastSymbol which maps the positive instances of yesOnString to positive instances of lastSymbol.
once we have this mapping, we can write a program yesViaLastSymbol which decides yesOnString using the output of lastSymbol. 
this is a contradiction since we know yesOnString is undecidable, therefore lastSymbol cannot be decidable 
'''
