

def processAxis(input, cutoff):
    if abs(input) < cutoff:
        return 0
    else:
        return input