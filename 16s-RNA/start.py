from cogent.db.ncbi import EUtils
from cogent.parse.fasta import MinimalFastaParser


def load_and_filter_seqs(seqs, domain_label):
    result = []
    for seq_id, seq in seqs:
        if len(seq) > 750 and seq.count('N') < 1:
            result.append((domain_label + seq_id,seq))
    return result


e = EUtils()
arc16s = list(MinimalFastaParser(e['"small subunit rRNA"[ti] AND archaea[orgn]']))
bac16s = list(MinimalFastaParser(e['"small subunit rRNA"[ti] AND bacteria[orgn]']))
euk16s = list(MinimalFastaParser(e['"small subunit rRNA"[ti] AND eukarya[orgn]']))

def label_to_name(x):
    fields = x.split()
    return '%s: %s' % (fields[3].split('/')[0], fields[0])

seqs = LoadSeqs(data=fasta_str.split('\n'),moltype=DNA,aligned=False,label_to_name=label_to_name)