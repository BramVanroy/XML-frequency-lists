# SONAR frequency lists
 - Sorted per component (cf. [component contents below](#sonar-components-contents))
 - Every component dir has two sub directories:
   - `with_pos/`: the POS tag of each keyword is included. This means that there is a distinction between homographs as
   long as they have different POS tags. The result is a frequency list with format `{token}\t{pos}\t{count}`
   - `without_pos/`: the POS tag is not included. This means that there is **no** distinction between homographs. The
   result is a frequency list with format `{token}\t{count}`
 - A file's name describes its content, format:
 `{component}[-withpos][-contentonly]-attr[-rmonlynonans][-rmonlydigits].freqs`:
   - `component`: the SONAR component
   - `-withpos`: whether or not POS tags are included (cf. supra)
   - `-contentonly`: only content words are included, i.e. POS (`pt` for SONAR) of nouns (`n`), adjectives (`adj`),
   adverbs (`bw`), and verbs (`ww`). Other word classes are discarded
   - `attr`: the most important: which XML attribute was used to gather frequencies from. E.g. in SONAR, for tokens
   `word`, for lemmata `lemma`
   - `-rmonlynonans`: all tokens that only consist of non-alphanumeric characters have been removed from the list
   - `-rmonlydigits`: all tokens that only consist of digits have been removed from the list (note: tokens such as
   `1,23` or `-3` are thus *not* removed, as it contains a non-digit character.)


# Build your own frequency lists
Attached script `xml_attrval_frequencies` serves as a great starting point to build your own frequency list from any
XML, POS-tagged corpus. Note that [**PyLT3**](https://github.com/BramVanroy/PyLT3) is required to run that script.   


# SONAR components contents
| Corpus   | Contents   | # sentences |
| :------- | :--------- | ----------: |
| WR-P-E-A | Discussion lists	4,395,094 |
| WR-P-E-C | E-magazines | 551,119 |
| WR-P-E-E | Newsletters | 115 |
| WR-P-E-F | Press releases | 18,372 |
| WR-P-E-G | Subtitles | 3,925,824 |
| WR-P-E-H | Teletext pages | 40,715 |
| WR-P-E-I | Websites | 204,998 |
| WR-P-E-J | Wikipedia | 1,354,245 |
| WR-P-E-K | Blogs | 8,614 |
| WR-P-E-L | Tweets | 2,636,859 |
| WR-P-P-B | Books | 1,709,808 |
| WR-P-P-C | Brochures | 74,897 |
| WR-P-P-D | Newsletters | 2,184 |
| WR-P-P-E | Guides & manuals | 19,077 |
| WR-P-P-F | Legal texts | 650,211 |
| WR-P-P-G | Newspapers | 14,973,209 |
| WR-P-P-H | Periodicals & magazines | 5,475,556 |
| WR-P-P-I | Policy documents | 387,312 |
| WR-P-P-J | Proceedings | 16,935 |
| WR-P-P-K | Reports | 93,507 |
| WR-U-E-A | Chats | 2,387,131 |
| WR-U-E-D | SMS | 101,116 |
| WR-U-E-E | Written assignments | 23,488 |
| WS-U-E-A | Auto cues | 2,163,521 |
| WS-U-T-B | Texts for the visually impaired | 44,862 |
| **SoNaR** treebank | **Complete treebank** | **41,258,769** |
