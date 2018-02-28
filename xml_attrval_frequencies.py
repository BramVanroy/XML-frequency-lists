from pathlib import Path

from pylt3.xml_helpers import get_attr_frequencies
from pylt3.file_helpers import scan_dir_and_execute, print_tuplelist
from pylt3.type_helpers import sort_simple_dict, clean_simple_dict

"""
usage: xml_tag_frequencies.py [-h] [-c] [-p] input_dir tag attr

positional arguments:
  input_dir           main directory that contains corpus XML files
  tag                 XML tag that contains the XML attribute (in Alpino XML,
                      that is `node`)
  attr                XML attribute whose value is used to create the
                      frequency list

optional arguments:
  -h, --help          show this help message and exit
  -c, --content_only  flag to only calculate frequencies of content words
                      (nouns, adjectives, adverbs, verbs)
  -p, --include_pos   flag to also include the POS value of each token in the
                      frequency list
"""


def get_all_freqlists(input_file, xml_tag, xml_attr, content_only, include_pos):
    # SONAR POS tag is `pt`
    # Content words are POS n, adj, bw, and ww (noun, adjective, adverb, verb)
    if content_only:
        freqs = get_attr_frequencies(input_file, [xml_tag], xml_attr, normalize_capitalisation=True,
                                     restrict_to_pos=['n', 'adj', 'bw', 'ww'], include_pos=include_pos, pos='pt')
    else:
        freqs = get_attr_frequencies(input_file, [xml_tag], xml_attr, normalize_capitalisation=True,
                                     include_pos=include_pos, pos='pt')

    # string to append to filename, is this content only or not
    contentstr = '-contentonly' if content_only else ''
    # string to append to filename, does the output include pos tags or not
    withposstr = '-withpos' if include_pos else ''

    # Excludes tokens that consist only of non-alphanumeric characters (e.g. punctuation, space)
    freqs_only_nonan = clean_simple_dict(freqs, rm_only_nonan=True)
    # Excludes tokens that consist only of digits
    freqs_only_nonan_only_digits = clean_simple_dict(freqs, rm_only_digits=True, rm_only_nonan=True)

    # Given input files such as WRPPE.xml, get the component name WRPEE
    component = Path(input_file).stem

    # Use parent directory as corpus name 
    corpus = Path(input_file).parts[-2]

    if include_pos:
        base = Path('frequency-lists', corpus, component, 'with_pos')
    else:
        base = Path('frequency-lists', corpus, component, 'without_pos')

    # Create dir if it doesn't exist
    Path(base).mkdir(parents=True, exist_ok=True)

    freqs = sort_simple_dict(freqs, sort_on='values', reverse=True)
    freqs_only_nonan = sort_simple_dict(freqs_only_nonan, sort_on='values', reverse=True)
    freqs_only_nonan_only_digits = sort_simple_dict(freqs_only_nonan_only_digits, sort_on='values', reverse=True)

    # Print dictionaries to files
    print_tuplelist(freqs, base / f"{component}{withposstr}{contentstr}-{xml_attr}.freqs",
                    encoding='utf-8')
    print_tuplelist(freqs_only_nonan,
                    base / f"{component}{withposstr}{contentstr}-{xml_attr}-rmonlynonans.freqs",
                    encoding='utf-8')
    print_tuplelist(freqs_only_nonan_only_digits,
                    base / f"{component}{withposstr}{contentstr}-{xml_attr}-rmonlynonans-rmonlydigits.freqs",
                    encoding='utf-8')

    print(f"{component}: done!")

    return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", help="main directory that contains corpus XML files")
    parser.add_argument("tag", help="XML tag that contains the XML attribute (in Alpino XML, that is `node`)")
    parser.add_argument("attr", help="XML attribute whose value is used to create the frequency list")

    parser.add_argument("-c", "--content_only",
                        help="flag to only calculate frequencies of content words (nouns, adjectives, adverbs, verbs)",
                        action="store_true")
    parser.add_argument("-p", "--include_pos",
                        help="flag to also include the POS value of each token in the frequency list",
                        action="store_true")

    args = parser.parse_args()

    scan_dir_and_execute(args.input_dir, lambda file: get_all_freqlists(file, args.tag, args.attr, args.content_only,
                                                                        args.include_pos))
