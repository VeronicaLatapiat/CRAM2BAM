#!/usr/bin/env python
# coding: utf-8

# In[ ]:


conda update -n base -c defaults conda -y


# In[ ]:


conda install -c bioconda bcftools -y


# Sí, es posible realizar el procesamiento y análisis de variantes genéticas partiendo desde archivos CRAM de los pacientes. Los archivos CRAM son una alternativa comprimida y eficiente a los archivos BAM, que contienen los reads alineados a un genoma de referencia. Para utilizar archivos CRAM en el análisis de variantes genéticas y visualización de señales de reads en IGV, sigue estos pasos:

# Download CRAM

# In[ ]:


dx download Bulk/Exome\ sequences/Exome\ OQFE\ CRAM\ files/60/6003753_23143_0_0.cram


# In[ ]:


dx download Bulk/Exome\ sequences/Exome\ OQFE\ CRAM\ files/33/3369380_23143_0_0.cram


# In[ ]:


dx download Bulk/Exome\ sequences/Exome\ OQFE\ CRAM\ files/34/3482159_23143_0_0.cram


# trio 2

# In[ ]:


dx download Bulk/Exome\ sequences/Exome\ OQFE\ CRAM\ files/59/5962479_23143_0_0.cram


# In[ ]:


dx download Bulk/Exome\ sequences/Exome\ OQFE\ CRAM\ files/14/1401203_23143_0_0.cram


# In[ ]:


dx download Bulk/Exome\ sequences/Exome\ OQFE\ CRAM\ files/54/5474815_23143_0_0.cram


# trio 3

# In[ ]:


dx download Bulk/Exome\ sequences/Exome\ OQFE\ CRAM\ files/59/5995563_23143_0_0.cram


# In[ ]:


dx download Bulk/Exome\ sequences/Exome\ OQFE\ CRAM\ files/14/1482222_23143_0_0.cram


# In[ ]:


dx download Bulk/Exome\ sequences/Exome\ OQFE\ CRAM\ files/34/3407982_23143_0_0.cram


# Conversión a BAM

# In[ ]:


curl -O https://ftp.ncbi.nlm.nih.gov/1000genomes/ftp/technical/reference/GRCh38_reference_genome/GRCh38_full_analysis_set_plus_decoy_hla.fa


# verificar su contenido con el siguiente comando

# In[ ]:


cat GRCh38_full_analysis_set_plus_decoy_hla.fa


# In[ ]:


samtools faidx GRCh38_full_analysis_set_plus_decoy_hla.fa chr2 > chr2.fa
samtools faidx GRCh38_full_analysis_set_plus_decoy_hla.fa chr10 > chr10.fa
samtools faidx GRCh38_full_analysis_set_plus_decoy_hla.fa chr19 > chr19.fa
samtools faidx GRCh38_full_analysis_set_plus_decoy_hla.fa chrX > chrX.fa


# In[ ]:


cat chr2.fa chr10.fa chr19.fa chrX.fa > small.reference.fa


# In[ ]:


samtools view -b -T small.reference.fa -o bam_3369380_23143_0_0.bam 3369380_23143_0_0.cram


# In[ ]:


samtools index bam_3369380_23143_0_0.bam


# In[ ]:


samtools view -b -T small.reference.fa -o bam_3482159_23143_0_0.bam 3482159_23143_0_0.cram


# In[ ]:


samtools index bam_3482159_23143_0_0.bam


# In[ ]:


samtools view -b -T small.reference.fa -o bam_6003753_23143_0_0.bam 6003753_23143_0_0.cram


# In[ ]:


samtools index bam_6003753_23143_0_0.bam


# Carga de Datos en IGV:
# Abre IGV y selecciona un genoma de referencia adecuado.
# Carga los archivos BAM resultantes de la conversión de los archivos CRAM en IGV para visualizar los reads alineados.
# 

# Visualización en IGV:
# Explora las regiones de interés donde se encuentran las variantes genéticas.
# Utiliza las herramientas de zoom y navegación para examinar detalladamente las regiones específicas.

# Análisis de Variantes:
# Identifica las variantes genéticas en las regiones seleccionadas comparando los reads entre padres e hijos.
# Observa las diferencias y similitudes en las señales de los reads para comprender mejor las variantes presentes.
