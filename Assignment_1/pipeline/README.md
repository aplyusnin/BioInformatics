## Running pipeline

This pipeline should be triggered with params:

1. referece - File with genome reference
2. reades - Genome reads
3. temp - temporary file to store intermediate results.

In my case: 

    {
      "reference" : "~/EColi/reference.fna",
      "reads" : "~/EColi/sra_data.fastq.gz",
      "temp" : "~/EColi/tmp.sam"
    }
