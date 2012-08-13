brown_pos_converter
===================

I use this script to generate one big brown.pos to train part of speech models for natural language processing. It constructs one large easily parsable file with POS tagged sentences (one token per line and sentences separated by empty lines) from brown POS corpus files. This script ignores some fucked up sentences and performs token mappings like "I'm" -< "I" "am". 

Just set path where all your brown POS training files are and run it. You can also chose the token/tag separator-string TAG_TOKEN_SEPARATOR. 

Output with TAG_TOKEN_SEPARATOR='#!#' looks like this:

    The#!#at
    Fulton#!#np
    County#!#nn
    Grand#!#jj
    Jury#!#nn
    said#!#vbd
    Friday#!#nr
    an#!#at
    investigation#!#nn
    of#!#in
    Atlanta's#!#np$
    recent#!#jj
    primary#!#nn
    election#!#nn
    produced#!#vbd
    no#!#at
    evidence#!#nn
    that#!#cs
    any#!#dti
    irregularities#!#nns
    took#!#vbd
    place#!#nn
    .#!#.

    The#!#at
    jury#!#nn
    further#!#rbr
    said#!#vbd
    in#!#in
    term-end#!#nn
    presentments#!#nns
    that#!#cs
    the#!#at
    City#!#nn
    Executive#!#jj
    Committee#!#nn
    ,#!#,
    which#!#wdt
    had#!#hvd
    over-all#!#jj
    charge#!#nn
    of#!#in
    the#!#at
    election#!#nn
    ,#!#,
    deserves#!#vbz
    the#!#at
    praise#!#nn
    and#!#cc
    thanks#!#nns
    of#!#in
    the#!#at
    City#!#nn
    of#!#in
    Atlanta#!#np
    for#!#in
    the#!#at
    manner#!#nn
    in#!#in
    which#!#wdt
    the#!#at
    election#!#nn
    was#!#bedz
    conducted#!#vbn
    .#!#.

    ...
