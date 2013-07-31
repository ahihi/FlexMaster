import random

prefixes = (
    u"Accu",
    u"Flex",
    u"Multi",
    u"Sync",
    u"Ultra",
    u"View",
)
suffixes = (
    u"Master",
    u"Scan",
    u"Sharp",
    u"Sonic",
    u"Sync",
)

print random.choice(prefixes) + random.choice(suffixes)