#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH -t 1-
#SBATCH -J mesa_install
#SBATCH --mail-type=ALL
#SBATCH --mem-per-cpu=16G
#SBATCH --array=1-5

export MESA_DIR=/gpfs/gibbs/project/bellinger/sk3365/Mesa/mesa

export OMP_NUM_THREADS=24

export MESASDK_ROOT=/gpfs/gibbs/project/bellinger/sk3365/Mesa/mesasdk

source $MESASDK_ROOT/bin/mesasdk_init.sh

export PATH=$PATH:$MESA_DIR/scripts/shmesa

echo '-------------------------------'
cd ${SLURM_SUBMIT_DIR}
echo ${SLURM_SUBMIT_DIR}
echo Running on host $(hostname)
echo Time is $(date)
echo Mesa directory: $(MESA_DIR)
echo Mesa SDK directory: $(MESASDK_ROOT)
echo '-------------------------------'
echo -e '\n\n'

module load Python
module load make/4.3-GCCcore-10.2.0 Perl/5.32.0-GCCcore-10.2.0 X11/20201008-GCCcore-10.2.0 zlib/1.2.11-GCCcore-10.2.0 binutils/2.35-GCCcore-10.2.0 tcsh/6.22.03-GCCcore-10.2.0

mkdir Work/$SLURM_ARRAY_TASK_ID
cp -a Work/default/. Work/$SLURM_ARRAY_TASK_ID/

Python rspLinearCalculations.py