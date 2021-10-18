#!/bin/bash

#VAR="fna"

#if [! -f $1.$VAR]; then
#   $EXT = "fa"
#   if [! -f $1.$VAR]; then
#     echo "FILE NOT FOUND"
#     exit 1
#   fi
#fi
#bwa index $1.$VAR
#bwa mem $1.$VAR $2.fastq.gz > res.sam
TMP=$(samtools flagstat res.sam | head -n 5 | tail -1 | grep -o -P '[0-9]*(\.[0-9]*)?(?=%)')
echo $TMP
if (($(echo $TMP">90" | bc -l))); then
  echo "OK"
else
  echo "Not OK"
fi
