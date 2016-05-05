#!/bin/bash
: <<'END'

for i in $(<taxon_id)
do 
    name=$(basename "$i")
    epost -db taxonomy -id $i | elink -target nuccore | efetch -format fasta > id.fa.tmp
    perl -pe 'if(/\>/){s/\n/\t/}; s/\n//; s/\>/\n\>/' id.fa.tmp | perl -pe 's/\t/\n/' | tail -n+2 > tmp
    mv tmp id.fa && rm id.fa.tmp
    cat id.fa | perl -pe 'if(/\>/){s/\n/\#/g}' | grep NC_ | grep -vi plasmid | sed 's/#/\n/g'> $name\_nc.fa
    rm id.fa
    echo "done\n"
done
END

for i in $(<taxon_id)
do
    name=$(basename "$i")
    epost -db taxonomy -id $i | elink -target nuccore | efetch -format fasta > id.fa.tmp
    perl -pe 'if(/\>/){s/\n/\t/}; s/\n//; s/\>/\n\>/' id.fa.tmp | perl -pe 's/\t/\n/' | tail -n+2 > tmp
    mv tmp id.fa && rm id.fa.tmp
	cat id.fa | perl -pe 'if(/\>/){s/\n/\@/g}' | sed 's/|ref|/#ref$>/g' | grep \#ref\$\> | grep -v "ribosomal\|plasmid" | cut -d\$ -f2 | sed 's/@/\n/g'> $name\_nc.fa
    rm id.fa
    echo "Done $i"
done
