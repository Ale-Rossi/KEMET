#!/usr/bin/env python
# coding: utf-8

import argparse

def add_organism_instruction(fasta_file, taxonomy, universe, verbose=False):
    try:
        with open("genomes.instruction", "a") as f:
            print(fasta_file, taxonomy, universe, sep="\t", file=f)
    except FileNotFoundError:
        print("ERROR: genomes.instruction file missing - RUN setup.py")
        raise

    if verbose:
        print("COMPLETE organism instruction:")
        print(fasta_file, taxonomy, universe)


###############################################################################

def main():
    parser = argparse.ArgumentParser(description='''Add instructions of MAGs/Genomes of interest for KEMET analysis - required for HMM and GSMM operations''')

    parser.add_argument('-f','--add_fasta_file', required=True,
                        help='''Add info regarding MAG/Genome file name (with extension).''')
    parser.add_argument('-t','--add_taxonomy', required=True,
                        help='''Add info regarding MAG/Genome taxonomy.''') #TODO: PARSE THE INFO FROM SOME TAXONOMY FILE?
    parser.add_argument('-u','--add_universe', default="",
                        help='''Add info regarding the metabolic universe to which the organism belong (WHEN TO USE: further metabolic reconstruction).''')
    parser.add_argument('-v','--verbose', action="store_true",
                        help='''Print more informations - for debug or log.''')

    args = parser.parse_args()

###############################################################################

    add_organism_instruction(args.add_fasta_file,
                             args.add_taxonomy,
                             args.add_universe,
                             args.verbose)


if __name__ == "__main__":
    main()

