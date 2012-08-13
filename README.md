brown_pos_converter
===================

I use this script to generate one big brown.pos to train part of speech models for natural language processing. It constructs one large easily parsable file with POS tagged sentences (one token per line) from brown POS corpus files. This script ignores some fucked up sentences and performs token mappings like "I'm" -< "I" "am". 

Just set path where all your brown POS training files are and run it. You can also chose the token/tag separator-string TAG_TOKEN_SEPARATOR. 

