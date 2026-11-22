from dataclasses import dataclass, field

@dataclass
class SymbolData:
    symbol: str
    proposed_sound: str = "?"
    consonant: bool = False # appears in at least one V?V
    vowel: bool = False     # appears in at least one C?C
    bridge: bool = False    # appears in at least one C?V or V?C
    sequence_strings: set = field(default_factory=set)

l_sound = "E"
#l_sound = "R"

master_symbol_list = [

    ### VOWELS

    ## <a> looks like a cursive "a".
    SymbolData("a", "A", vowel=True),

    ## <y> looks like <a> but with a word-final down hook, kind of like a 9.
    SymbolData("y", "A", vowel=True),

    ## <u> looks like <a> but with a word-final up hook.
    SymbolData("u", "A", vowel=True),

    ## <o> looks just like "o".
    SymbolData("o", "O", vowel=True),

    ### "C" VARIANTS

    ## <e> looks just like "c".
    SymbolData("e", "U"),

    ## <ee> looks just like "cc".
    SymbolData("ee", "UU"),

    ## <eee> looks just like "ccc".
    SymbolData("eee", "UUU"),

    ## <eeee> looks just like "cccc".
    SymbolData("eeee", "UUUU"),

    ## <b> looks like a "c" with a word-final up hook.
    SymbolData("b", "U"),

    ## <eb> looks like "cc" with a word-final up hook.
    SymbolData("eb", "UU"),

    ## <eeb> looks like "ccc" with a word-final up hook.
    SymbolData("eeb", "UUU"),

    ## <eeeb> looks like "cccc" with a word-final up hook.
    SymbolData("eeeb", "UUUU"),

    ## <g> is a ligature of <ul>
    SymbolData("g", "U" + l_sound),

    ## <s> is like a backwards S, or a "c" with a top curl.
    SymbolData("s", "V", consonant=True),

    ### "I" VARIANTS
        
    ## <i> looks like "i", tilted, with no dot.
    SymbolData("i", "I"),

    ## <n> looks like "i" followed by a word-final up-hook.
    SymbolData("n", "I"),

    ## <ii> looks like "ii".
    SymbolData("ii", "II"),

    ## <iii> looks like "iii".
    SymbolData("iii", "III"),

    ## <in> looks like "ii" followed by a word-final up-hook.
    SymbolData("in", "II"),

    ## <iin> looks like "iii" followed by a word-final up-hook.
    SymbolData("iin", "III"),

    ## <iiin> looks like "iiii" followed by a word-final up-hook.
    SymbolData("iiin", "IIII"),

    ## <m> is a ligature of <il>
    SymbolData("m", "I" + l_sound),

    ## <im> is a ligature  of <iil>
    SymbolData("im", "II" + l_sound),

    ## <r> looks like an with a curl on top, or like a scythe with a handle and blade.
    SymbolData("r", "J", consonant=True),

    ### GALLOWS AND BENCH

    ## <ch> is the bench letter.
    SymbolData("ch", "S", consonant=True),

    ## <sh> is the bench letter with a loop on top.
    SymbolData("sh", "SH", consonant=True),

    ## <t> is the "ll"-like gallows letter with both connecting loops.
    SymbolData("t", "T", consonant=True),

    ## <k> is the "ll"-like gallows letter with the left connecting loop missing
    SymbolData("k", "T", consonant=True),

    ## <z> is a diminutive <k> that appears one time.
    SymbolData("z", "T", consonant=True),

    ## <cth> is the complete gallows letter combined with the bench.
    SymbolData("cth", "TH", consonant=True),

    ## <cthh> is complete gallows combined with bench followed by a "c" that may be attached to the bench.
    SymbolData("cthh", "TH", consonant=True),

    ## <ckh> is the incomplete gallows letter combined with the bench.
    SymbolData("ckh", "TH", consonant=True),

    ## <c> is a bench, but the right half of the bench is missing.
    SymbolData("c", "s", consonant=True),

    ## <c> is a bench, but the left half of the bench is missing.
    SymbolData("h", "s", consonant=True),

    ## <p> is the "P"-like gallows letter.
    SymbolData("p", "K", consonant=True),

    ## <f> is the same as <p> but the first loop is missing.
    SymbolData("f", "K", consonant=True),

    ## <cph> is the F gallows letter combined with the bench.
    SymbolData("cph", "KH", consonant=True),

    ## <cfh> is the incomplete F gallows letter combined with the bench.
    SymbolData("cfh", "KH", consonant=True),

    ## <cfhh> is an incomplete F gallows combined with bench followed by a "c" that may be attached to the bench.
    SymbolData("cfhh", "KH", consonant=True),

    ## <cphh> is an complete F gallows combined with bench followed by a "c" that may be attached to the bench.
    SymbolData("cphh", "KH", consonant=True),

    ### OTHERS

    ## <l> looks like cursive "l", or an awareness ribbon character, or a tilted "e".
    SymbolData("l", l_sound, consonant=True),

    ## <d> is the 8 letter.
    SymbolData("d", "P", consonant=True),

    ## <j> looks just like <d>.
    SymbolData("j", "P", consonant=True),

    ## <q> looks like a 4 or g.
    SymbolData("q", "H", consonant=True),

    ## <x> looks like a little two-legged stool that only appears 43 times.
    SymbolData("x", "R", consonant=True),

    ## <,> means they"re not sure if there"s a space or not.
    SymbolData(",", ","),

    ## <?> means they"re not sure what letter it is.
    SymbolData("?", "?"),
]

# Collect various data as we scan the file.
from collections import defaultdict

# Match on the longest symbols first. <iin> should match before <i>.
sorted_symbol_list = sorted(master_symbol_list, key=lambda item: len(item.symbol), reverse=True)

import re

final_counts = defaultdict(int)
initial_counts = defaultdict(int)
medial_counts = defaultdict(int)
counts = defaultdict(int)
word_counts = defaultdict(int)

# Create a translation of the source file for reference.
with open("RF1a-n_translation.txt", "w", encoding="utf-8") as output_file:
    with open("RF1a-n.txt", "r", errors="replace") as source_file:
        page = ""
        character_type_list = dict()
        for line in source_file:
            print(line, end="", file=output_file)
            line = line.strip()
            #   <f1r>      <! $Q=A $P=A $F=a $B=1 $I=T $L=A $H=1 $C=1 $X=V>
            match = re.match(r"^<f\d+.>", line)
            if match:
                # if page:
                #     for symbol_data in character_type_list.values():
                #         print(f"\t<{symbol_data.symbol}>", end="", file=output_file)
                #         if symbol_data.consonant:
                #             print(f" consonant", end="", file=output_file)
                #         if symbol_data.vowel:
                #             print(f" vowel", end="", file=output_file)
                #         if symbol_data.bridge:
                #             print(f" bridge", end="", file=output_file)
                #         print(file=output_file)
                #         formatted_sequence_strings = " ".join(symbol_data.sequence_strings)
                #         print(f"\t\t{formatted_sequence_strings}", file=output_file)
                page = match.group()
                character_type_list = dict()
                continue
            #   <f1v.5,+P0>       potoy.shol.jair.cphoal<->dar.chey.tody.otoaiin.shosh
            if not re.match(r"^<.*,.*>", line):
                continue
            left_part, right_part = line.split(">", 1)
            right_part = right_part.strip()
            translated_line = "                   "
            words = re.split(r"\.|<->", right_part)
            for word in words:
                word_counts[word] += 1
                # Translate the word into our proposed sounds and put in file:
                translated_word = ""
                word_data = [SymbolData(".")]
                i = 0
                while i < len(word):
                    matched = False
                    for data in sorted_symbol_list:
                        if word[i:].startswith(data.symbol):
                            translated_word += data.proposed_sound
                            i += len(data.symbol)
                            matched = True
                            counts[data.symbol] += 1
                            word_data.append(data)
                            break
                    if not matched:
                        translated_word += "<?" + word[i] + "?>"
                        i += 1
                translated_line += translated_word + " "
                word_data.append(SymbolData("."))
                
                # Record whether each symbol must be a vowel or a consonant.
                i = 0
                while i < len(word_data) - 2:
                    previous_data = word_data[i + 0]
                    target_symbol = word_data[i + 1].symbol
                    next_data = word_data[i + 2]

                    if previous_data.symbol == '.':
                        initial_counts[target_symbol] += 1
                    if next_data.symbol == '.':
                        final_counts[target_symbol] += 1
                    if previous_data.symbol != '.' and next_data.symbol != '.':
                        medial_counts[target_symbol] += 1

                    if target_symbol not in character_type_list:
                        character_type_list[target_symbol] = SymbolData(target_symbol)
                    
                    sequence_string = f"{previous_data.symbol}{target_symbol}{next_data.symbol}"
                    character_type_list[target_symbol].sequence_strings.add(sequence_string)

                    if previous_data.consonant and next_data.consonant:
                        character_type_list[target_symbol].vowel = True
                    if previous_data.vowel and next_data.vowel:
                        character_type_list[target_symbol].consonant = True
                    if previous_data.consonant and next_data.vowel:
                        character_type_list[target_symbol].bridge = True
                    if previous_data.vowel and next_data.consonant:
                        character_type_list[target_symbol].bridge = True
                    i += 1
                
            print(translated_line.upper(), file=output_file)

    print("\nsymbol counts", file=output_file)
    for symbol_data in master_symbol_list:
        print(f"{symbol_data.symbol}\t{initial_counts[symbol_data.symbol]}\t{medial_counts[symbol_data.symbol]}\t{final_counts[symbol_data.symbol]}", file=output_file)

    print("\ncounts", file=output_file)
    for symbol, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{symbol}\t{count}", file=output_file)
    
    print("\nword counts", file=output_file)
    for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}\t{count}", file=output_file)
        if count < 2:
            break
    
